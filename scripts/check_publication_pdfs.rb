#!/usr/bin/env ruby
# frozen_string_literal: true

# Verifies that every publication in _data/publications.yaml (that lists
# La Cava as an author, matching the filter in _pages/papers.md) has a
# matching PDF checked into assets/papers/. Filenames are derived with the
# exact same logic as _includes/pub-single.html so this stays in sync with
# what the site actually links to (and with Zotero's own "Rename Associated
# File" convention: "{Author(s)} - {Year} - {Title, 50 chars}.pdf").
#
# Usage:
#   ruby scripts/check_publication_pdfs.rb            # error on missing PDFs
#   ruby scripts/check_publication_pdfs.rb --list      # just list, exit 0

require 'yaml'
require 'pathname'

ROOT = Pathname.new(__dir__).parent
DATA_FILE = ROOT / '_data' / 'publications.yaml'
PAPERS_DIR = ROOT / 'assets' / 'papers'

def author_surname(author)
  return author['literal'] if author['literal']

  particle = author['non-dropping-particle']
  family = author['family']
  [particle, family].compact.join(' ').strip
end

def by_cava?(pub)
  Array(pub['author']).any? do |author|
    (author['family'] || '').include?('Cava') || (author['literal'] || '').include?('Cava')
  end
end

def pdf_author(pub)
  authors = Array(pub['author'])
  first = author_surname(authors[0])
  case authors.size
  when 0 then ''
  when 1 then first
  when 2 then "#{first} and #{author_surname(authors[1])}"
  else "#{first} et al."
  end
end

# Mirrors Liquid's `truncate: 50, ''` followed by `strip`.
def pdf_title(pub)
  title = (pub['title'] || '').to_s
  truncated = title.length > 50 ? title[0, 50] : title
  truncated.strip
end

def expected_filename(pub)
  year = pub.dig('issued', 0, 'year')
  base = "#{pdf_author(pub)} - #{year} - #{pdf_title(pub)}.pdf"
  base.delete(':').delete('?')
end

data = YAML.load_file(DATA_FILE)
refs = data['references'] || []
cava_refs = refs.select { |pub| by_cava?(pub) }

missing = cava_refs.filter_map do |pub|
  filename = expected_filename(pub)
  path = PAPERS_DIR / filename
  [pub['id'], filename] unless path.exist?
end

list_only = ARGV.include?('--list')

if missing.empty?
  puts "All #{cava_refs.size} publication PDFs are present in #{PAPERS_DIR.relative_path_from(ROOT)}."
  exit 0
end

warn "#{missing.size} publication#{'s' if missing.size != 1} missing a PDF in #{PAPERS_DIR.relative_path_from(ROOT)}:"
missing.each do |id, filename|
  warn "  - [#{id}] #{filename}"
end

exit(list_only ? 0 : 1)
