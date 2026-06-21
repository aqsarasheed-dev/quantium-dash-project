 🍩 Pink Morsel Sales Dashboard

An interactive data visualisation tool built for **Soul Foods** to analyse the impact of the Pink Morsel price increase on the 15th of January, 2021.

This project processes raw transactional CSV files, transforms them into a clean dataset, and displays the results in a modern, responsive Dash web application.

---

📊 The Business Question

 “Were sales of Pink Morsels higher before or after the price increase on January 15, 2021?

This dashboard answers that question instantly for all regions combined or for individual regions  using a clear line chart and a dynamic summary box.

---

✨ Features

Data Processing: Merges 3 raw CSV files, filters for `"pink morsel"`, calculates daily sales (`quantity * price`), and outputs a single clean CSV. |
Interactive Line Chart: Visualises total daily sales over time with a clear marker for the price change date. 
Region Filtering :Five radio buttons (`All`, `North`, `East`, `South`, `West`) instantly update the chart and summary. |
Smart Summaries: A dynamic text box shows exactly whether sales increased or decreased after the price change, with average values. |
Custom Colour Palette :Styled with a cohesive, modern colour scheme: `#FEE3F4`, `#B3DFF9`, `#97D4FA`, `#E1E7FA`, `#575461`, and `#102919`. |
Clean UI : Inspired by modern Dash galleries (like the Brain Viewer), with hover effects, soft shadows, and a professional layout. |

---

## 🛠️ Tech Stack

- Python 3.9
- Dash – Web framework for the interactive dashboard
- Plotly – Interactive charting library
- Pandas – Data processing and manipulation
- Git – Version control


```bash
git clone https://github.com/YOUR_USERNAME/quantium-dash-project.git
cd quantium-dash-project
