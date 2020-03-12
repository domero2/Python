#Generate file with sequence of the same description and only table name changes based on list of table names
list1=['Table1',
Table2,
Table3]

with open( "/Users/amajcher/Desktop/Python/NewFiles/SQL_FOR_REPORTS.sql", "w") as file:
    for i in list1:
        file.write(f'''select TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM {SchemaName}.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = \"{i}\"
and TABLE_SCHEMA='dbo';\n''')

#Generate separate files with sequence of the same description and only table name changes based on list of table names

list2=['Table1',
Table2,
Table3]

for i in list2:
    with open( "/Users/amajcher/Desktop/Python/Generate_files/audit_table_{}.txt".format(i), "w") as file:
        file.write(f'''select TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM {SchemaName}.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = \"{i}\"
and TABLE_SCHEMA='dbo';\n''')
