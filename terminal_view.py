from rich.console import Console
from rich.markdown import Markdown

md_text = """
## Study Plan

- **ENGLISH**
- **SCIENCE**  
  - DE: SQL, Py, PySpark, Git, Pipelines, Cloud, Construction  
  - DS: Business, Statistics and Math, Languages, Automatic, Cloud, ML, Viz, Practice
- *(in progress)* Productivity on YouTube
- *(in progress)* Data Project: [Tendence](https://tendence.up.railway.app/)
- *(in progress)* SQL: [link0](https://www.youtube.com/watch?v=G7bMwefn8RQ...), [link1](https://www.youtube.com/playlist?...), [link2](https://www.youtube.com/playlist?...)
"""

console = Console()
console.print(Markdown(md_text))
