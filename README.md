# Zootopia with API

This project generates an HTML page that displays animal information fetched from the API Ninjas animal API. It is an extended version of the original "Zootopia" project, now supporting live API data and a modular file structure.

## Installation

To install and run this project locally:

1. Clone the repository  
2. Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your API key:

```env
API_KEY=your_api_key_here
```

## Usage

To generate the HTML output:

```bash
python animals_web_generator.py
```

The file `animals.html` will be generated with up-to-date animal information.

## Project Structure

- `data_fetcher.py` – Fetches data from the API
- `animals_web_generator.py` – Loads the template and builds the HTML page
- `animals_template.html` – Template HTML file where animal info will be inserted

## Contributing

Contributions are welcome!  
If you'd like to contribute to this project:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Commit your changes with clear messages
4. Push to your branch and open a pull request

Please ensure your code follows standard Python practices and includes helpful comments or docstrings.

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Michael

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
