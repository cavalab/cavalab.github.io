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

require_relative 'lib/publication_pdfs'

missing = PublicationPdfs.missing_pdfs
list_only = ARGV.include?('--list')
papers_dir = PublicationPdfs::PAPERS_DIR.relative_path_from(PublicationPdfs::ROOT)

if missing.empty?
  puts "All #{PublicationPdfs.cava_refs.size} publication PDFs are present in #{papers_dir}."
  exit 0
end

warn "#{missing.size} publication#{'s' if missing.size != 1} missing a PDF in #{papers_dir}:"
missing.each do |pub|
  warn "  - [#{pub[:id]}] #{pub[:filename]}"
end

if !list_only
  warn ''
  warn 'Tip: ruby scripts/find_missing_pdfs.rb will search your Zotero storage for candidates.'
end

exit(list_only ? 0 : 1)
