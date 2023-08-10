# broken-link-checker

broken-link-checker is a tool developed using the Scrapy web crawling framework
in Python. Its purpose is to help users detect broken links (invalid links) on a
specified website. Broken links can have a negative impact on user experience
and search engine rankings, making timely detection and fixing of these links
crucial.

The tool provides a simple yet powerful way to crawl a given website and analyze
its pages, identifying any broken links present. It supports exporting the
detection results to a CSV file, facilitating further analysis and handling by
users.

## Installation

To use the broken-link-checker tool, you need to meet the following
requirements:

- Python 3.x
- Scrapy library
- Other dependency libraries (list specific dependencies and provide
  installation instructions)

Once you have the required environment set up, you can follow these steps to
install and run the tool:

1. Clone the project repository
2. Navigate to the project directory: `cd broken-link-checker`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage Instructions

Navigate to your project directory and run the spider using the following
command:

```bash
scrapy crawl broken_link_spider -a domain=example.com -a url=http://www.example.com -o broken_links.csv
```

This command will start the spider and save the results in a CSV file named
broken_links.csv.

Remember to replace 'example.com' with the actual domain you want to check for
broken links, and adjust the starting URL if needed.

This will only save links to the CSV file if the status code is 404. Make sure
the fields in the CSV file match the fields defined in items.py. If there are
still questions, please elaborate on your needs and problems and I will try to
help more accurately.

## Notes

Please be aware that using this tool may exert slight access pressure on the
target website; please use responsibly within reasonable limits. This tool is
provided as-is, and we are not responsible for any issues caused by its use.

## Contributions

If you discover any issues or opportunities for improvement, feel free to raise
an Issue or submit a Pull Request. Your contributions are greatly appreciated!

## License

This project is open-source under the Apache License 2.0.
