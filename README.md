HXL hashtag lookup
==================

Compile and use a model for matching text headers to HXL hashtags.

For more information about HXL, see https://hxlstandard.org

## Requirements

- Python 3
- libhxl

Use the command

    $ pip3 install -r requirements.txt
    
to install the requirements.

## Usage

This package uses the output from https://github.com/HXLStandard/hdx-hashtag-crawler

The distribution includes a snapshot in inputs/ (but you can create your own, fresher one)

### Command-line usage

    $ python3 -m hxltags.compiler inputs/20200720-hxl-tags-atts.csv > my-model.json
    $ python3 -m hxltags.lookup my-model.json
    
### Python usage

    import hxltags.compiler, hxltags.lookup
    
    model = hxltags.compiler.build_model("inputs/20200720-hxl-tags-atts.csv")
    
    results = hxltags.lookup.lookup_header("Number of people affected", model)

## License

This code is in the Public Domain. See UNLICENSE.md for details.

## Author

David Megginson, Centre for Humanitarian Data, UNOCHA
