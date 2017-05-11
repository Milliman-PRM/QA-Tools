"""
### CODE OWNERS: Steve Gredell
### OBJECTIVE: Parse checklists into TestRail test cases
### DEVELOPER NOTES:
  I'm lazy so you'll have to copy/paste the input and output files at the top of the script
"""
import xml.etree.cElementTree as ET
from pathlib import Path
checklist = Path(r"C:\Users\steve.gredell\repos\analytics-pipeline\800_QlikView_QVWs\_Checklists\PRCA_Report_Checklist.txt")
xml_out = Path(r"C:\Users\steve.gredell\repos\analytics-pipeline\800_QlikView_QVWs\_Checklists\PRCA_Report_Checklist.xml")

# root = ET.Element("suite")
# name = ET.SubElement(root, "name")
# name.text = "Care Coordinator Report"
# desc = ET.SubElement(root, "description")
sections = ET.Element("sections")
step_index = 1
with checklist.open() as cl:
    for line in cl:
        if line[0] == '!':
            section = ET.SubElement(sections, "section")
            sec_name = ET.SubElement(section, "name")
            sec_name.text = line[1:].rstrip()
            ET.SubElement(section, "description")
            cases = ET.SubElement(section, "cases")
        elif line[0] == '|':
            step = ET.SubElement(steps_separated, "step")
            index = ET.SubElement(step, "index")
            index.text = str(step_index)
            step_index += 1
            ET.SubElement(step, "content")
            expected = ET.SubElement(step, "expected")
            expected.text = line[1:].rstrip()
        elif line[0] == '(':
            pass  # ignore comment line
        elif line[0] == '\n':
            pass  # ignore blank lines
        elif line[0] == '*':
            # desc.text = "".join(['*', line[2:].rstrip()])
            pass
        elif line[0:2] == '-|':
            # This is a SQL statement, put it in the "prerequisites" section
            preconds.text = "".join(["`", line[2:].replace('^nl', '\n').rstrip(), "`"])
        else:
            case = ET.SubElement(cases, "case")
            ET.SubElement(case, "id")
            title = ET.SubElement(case, "title")
            title.text = line.rstrip()
            template = ET.SubElement(case, "template")
            template.text = "Test Case (Steps)"
            ET.SubElement(case, "type")
            ET.SubElement(case, "priority")
            ET.SubElement(case, "estimate")
            ET.SubElement(case, "milestone")
            ET.SubElement(case, "references")
            custom = ET.SubElement(case, "custom")
            preconds = ET.SubElement(custom, "preconds")
            steps_separated = ET.SubElement(custom, "steps_separated")
            step_index = 1  # reset step index when creating a new test case

tree = ET.ElementTree(sections)
tree.write(str(xml_out))
