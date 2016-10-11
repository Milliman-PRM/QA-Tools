#Building the Checklist
*	Open the 'QVW Review Checklist Builder.xlsm' in your repo
*	Click on "Build Checklist" button
*	Copy the .qvw path of the report you are checking and paste into QVW Network Location
*	Paste in the QVW URL that is related to the report you are checking
*	Build Checklist


#Checklist for Checklists
These are tips for creating checklists and what to include for the different types of objects


###List Boxes
*	Default sort for list box (which field is driving the default sort order)
*	Indicate whether selections made in the list box move to the top or are stationary
*	Selections made in the list box are correctly reflected in the Current Selections bar/dropdown
*	When a selection is made, the label of the list box is used in the Current Selections bar/dropdown to reflect the selection
*	Selections made in the list box change the number of patients returned at the top
*	Explicitly say which list boxes should be visible always, and which are conditionally shown and when
*	Include the formats with which the numbers should be displayed
*	The percentages add up to ~100%
*	If there are bars, the bars appear to match the percentages shown in the list box


###Tables
*	Include which fields should be found in tables
*	Default sort for table (which field is driving the default sort order)
*	Other fields sort order
*	Explicitly say which fields in the table should not be able to be filtered on or sorted by
*	Explicitly say which fields in the table should be visible always, and which are conditionally shown and when
*	Include the formats with which the numbers should be displayed
*	Include information about the fields with dropdowns (when a little black downward facing arrow should be visible)


###Tabs
*	State which tabs should be selected by default when entering the report
*	List out situations when tabs are accessible and non-accessible
*	Indicate when a tab should have a color change


#Clarifying Field Names#
The Filter Population page in particular has various names that are displayed in certain list boxes. This is due to the difference in naming conventions for each client. Here is a list of some names that may occur for the fields listed:

* elig\_status\_1 (located in the top left corner)
  * Beneficiary Status
  * Dependent Status
  * Subscriber Relationship
  * Program Description
  * Population

* elig\_status\_2 (located below elig\_status\_1)
  * Hospice
  * Newly Assigned
  * New This Month

* assignment\_indicator (located below High ER Utilizer)
  * Attributed Patient
  * Assigned Patient

* prv\_hier\_1 (located to the right of elig\_status\_1)
  * Location
  * Group Name
  * Practice
  * Care Coordinator
  * Organization
  
* prv\_name (located below prv\_hier\_1)
  * Physician
  * Assigned Provider
  * Attributed Provider
  * Clinic
  * Practice
  * NP/RN
