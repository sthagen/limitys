# Usage

## Help Screen

```console
❯ limitys
usage: limitys [-h] [--language LANGUAGE] [--documents DOCUMENTS] [--out-path OUT_PATH] [--quiet] [--verbose] [documents_pos]

Overlap (Finnish: limitys) assesses sentences from constrained and overlapping vocabularies.

positional arguments:
  documents_pos         file with format in (json, yaml) providing the keyed documents. Optional
                        (default: documents.yml)

options:
  -h, --help            show this help message and exit
  --language LANGUAGE, -l LANGUAGE
                        language in (english, french, german, spanish) of the documents. Optional
                        (default: english)
  --documents DOCUMENTS, -d DOCUMENTS
                        file providing the keyed documents. Optional
                        (default: positional documents value)
  --out-path OUT_PATH, -o OUT_PATH
                        output file path for matrix (default: STDOUT)
  --quiet, -q           work as quiet as possible - progress bar only if all well (default: False)
  --verbose, -v         work logging more information along the way (default: False)
```

## Example

TBD
