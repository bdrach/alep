# -*- coding: utf-8 -*-
"""
    build.py
    ~~~~~~~~~~~~~~

    Converts ALEP restructured text files to html files.
    Now also copies static files to output directory.

"""
import codecs
import os
import re
import shutil
import sys
import urllib
import yaml
from argparse import ArgumentParser
from datetime import datetime
from docutils.core import publish_parts, publish_string
from jinja2 import Environment, FileSystemLoader


image_subdir = 'static/images/'
pdf_subdir = 'static/pdfs/'
lab_subdir = 'labs/'


class Converter(object):
    """ Base class for converting rst to html """

    def __init__(self, source_dir, dest_dir, root_dir):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.root_dir = root_dir

    def read_rst(self, filename):
        header_lines = []
        header_data = {}
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            header_line = f.readline().rstrip()
            if '---' in header_line:    # a header starts with ---, if exists
                header_line = f.readline().rstrip()
                while not '---' in header_line:
                    header_lines.append(header_line)
                    header_line = f.readline().rstrip()
                rst = ''.join(f.readlines()).encode('utf-8')
                header_data = yaml.load(os.linesep.join(header_lines))
                if header_data.get('title'): # Parse title to allow math
                    unparsed = header_data['title']
                    overrides = {'output_encoding': 'utf-8', 'math_output': 'MathJax'}
                    parsed = publish_parts(source=unparsed,
                                           writer_name='html',
                                           settings_overrides=overrides)
                    header_data['title'] = re.search(r'(?<=p>).*(?=</)', parsed['body']).group(0)
            else:    # no header, move back and parse rst
                f.seek(0)
                rst = f.read().encode('utf-8')
        rst = self.prepend_root_to_image_links(rst)
        return rst, header_data

    def write_html(self, html, filename):
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def rst_to_html(self, rst):
        overrides = {'output_encoding': 'utf-8', 'math_output': 'MathJax'}
        parts = publish_parts(source=rst,
                              writer_name='html4css1',
                              settings_overrides=overrides
                              )
        return parts['html_body']

    def prepend_root_to_image_links(self, rst):
        r = re.compile(r'images/[^.]+.png')
        matches = re.finditer(r, rst)
        for match in matches:
            match_index = match.start(0)
            short_link = match.group(0)
            image_name = os.path.basename(short_link.strip())
            full_link = os.path.join(self.root_dir.strip(), image_subdir, image_name)
            rst = rst[:match_index] + \
		  rst[match_index:].replace(short_link, full_link)
        return rst


class TopLevelPageConverter(Converter):
    def __init__(self, source_dir, dest_dir, root_dir, template):
        super(TopLevelPageConverter, self).__init__(source_dir, dest_dir, root_dir)
        self.home_template = template

    def run(self):
        for entry in os.listdir(self.source_dir):
            source_entry = os.path.join(self.source_dir, entry)
            if not source_entry.endswith('.rst'):
                if os.path.isfile(source_entry):
                    shutil.copy(source_entry, self.dest_dir)
                continue
            rst, header = self.read_rst(source_entry)
            html_body = self.rst_to_html(rst)
            html = self.home_template.render(body=html_body,
                                             title=header['title'],
                                             root_dir=self.root_dir,
                                             year=datetime.now().year)
            dest_file = os.path.join(self.dest_dir, entry.replace('.rst', '.html'))
            self.write_html(html, dest_file)


class LabConverter(Converter):
    """ Convert the projects and build index """
    def __init__(self, source_dir, dest_dir, root_dir,
                 lab_template, index_template):
        super(LabConverter, self).__init__(source_dir, dest_dir, root_dir)
        self.lab_template = lab_template
        self.index_template = index_template
        self.index = {}

    def write_lab_index(self):
        labs = {k:v for (k,v) in self.index.iteritems() \
                if v['type'] == 'lab'}
        exam_questions = {k:v for (k,v) in self.index.iteritems() \
                if v['type'] == 'exam_question'}
        html = self.index_template.render(labs=labs,
                                          exam_questions=exam_questions,
                                          root_dir=self.root_dir,
                                          title='Lab Index',
                                          year=datetime.now().year)
        dest_file = os.path.join(self.dest_dir, 'index.html')
        self.write_html(html, dest_file)

    def run(self):
        os.makedirs(os.path.join(self.dest_dir, lab_subdir))
        source_lab_dir = os.path.join(self.source_dir, lab_subdir)
        dest_lab_dir = os.path.join(self.dest_dir, lab_subdir)
        for entry in os.listdir(source_lab_dir):
            source_entry = os.path.join(source_lab_dir, entry)
            if not os.path.isfile(source_entry) or not source_entry.endswith('.rst'):
                continue
            rst, header = self.read_rst(source_entry)
            html_body = self.rst_to_html(rst)
            pdf_link = os.path.join(self.root_dir.strip(), pdf_subdir, header['id'] + '.pdf')
            html = self.lab_template.render(body=html_body,
                                            title=header['title'],
                                            root_dir=self.root_dir,
                                            pdf_link=pdf_link,
                                            year=datetime.now().year)
            dest_filename = header['id'] + '.html'
            lab_path = os.path.join(self.root_dir, lab_subdir, dest_filename)
            header['path'] = lab_path
            self.index[header['id']] = header
            dest_file = os.path.join(dest_lab_dir, dest_filename)
            self.write_html(html, dest_file)
        self.write_lab_index()


class RstToHtml:
    def __init__(self, source_rst_dir, templates_dir, dest_dir, local, root="/"):
        jinja_env = Environment(loader=FileSystemLoader(templates_dir))
        content_page_template = jinja_env.get_template('content_page.html')
        index_template = jinja_env.get_template('index.html')
        root_dir = os.path.join(os.getcwd(), dest_dir) if local else root

        self.home_converter = TopLevelPageConverter(source_rst_dir, dest_dir,
                                                    root_dir, content_page_template)
        self.lab_converter = LabConverter(source_rst_dir, dest_dir, root_dir,
                                          content_page_template, index_template)

    def run(self):
        self.home_converter.run()
        self.lab_converter.run()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('source', help='directory of source .rst files')
    parser.add_argument('templates', help='directory of source jinja2 template files')
    parser.add_argument('dest', help='desired location of generated site')
    parser.add_argument('--local', help='use absolute directory paths',
                        action="store_true")
    parser.add_argument('--root', help='use absolute directory paths',
                        nargs=1, default=["/"])
    args = parser.parse_args()
    converter = RstToHtml(args.source, args.templates, args.dest, args.local, args.root[0])
    converter.run()
