import os

print("This line will be printed.")

""" 
- Read Backup Definitions (XML) - fixed dir
    - Parse Definitions in backupDefinitions table (SQLite) - inc. raw XML

- Read Backup Log (HTML) - fixed dir
    = Split out the log part (XML)
    - Parse Backups into backupHeaders table (SQLite) - inc. raw XML

- Read Backup Files (OS) - dynamic dir based on definition files.
    - Identify root backup and mathc to backupHearders table (SQLite)
    - Parse Data about each backup file into the backupFiles table (SQLlite)
    - Check for deletions of any non-deleted backup file in table, and if missing from current files list, set deleted date, and 30 day expiry date. (SQLite)

- Summarize all of the information in current non-expired backupfiles into XML file (XML)  

- Build HTML page to explore XML data? (HTML)

- Save both XML and HTML to pre-determined "Backup informnation file"


 """