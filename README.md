# SSG - Static Site Generator

A Python-based static site generator developed as part of the backend development course on Boot.dev.

## Project Structure

```
.
├── src/
│   ├── main.py
│   ├── htmlnode.py
│   └── textnode.py
├── main.sh
└── test.sh
```

## Components

- `main.py`: Entry point of the application
- `htmlnode.py`: Defines the `HTMLNode` class for HTML element representation
- `textnode.py`: Defines the `TextNode` class (implementation not provided)

## Usage

To run the main script:

```bash
./main.sh
```

To run tests:

```bash
./test.sh
```

## Development

### HTMLNode Class

The `HTMLNode` class represents an HTML element with the following attributes:
- `tag`: HTML tag name
- `value`: Node value
- `children`: List of child nodes
- `props`: Dictionary of HTML attributes

Key methods:
- `to_html()`: Converts the node to HTML string (not implemented)
- `props_to_html()`: Converts props to HTML attribute string

## Requirements

- Python 3.x

## Testing

Tests are discovered and run using Python's unittest framework.