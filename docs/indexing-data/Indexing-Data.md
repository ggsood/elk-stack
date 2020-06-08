Things covered here

1. Define an Index That Satisfies a Given Set of Requirements
2. Perform Index, Create, Read, Update, and Delete Operations on the Documents of an Index
3. Define and Use Index Aliases
4. Define and Use an Index Template for a Given Pattern that Satisfies a Given Set of Requirements
5. Define and Use a Dynamic Template That Satisfies a Given Set of Requirements
6. Use the Reindex API and Update by Query API to Reindex and/or Update Documents --> create a secondary cluster
7. Define and Use an Ingest Pipeline That Satisfies a Given Set of Requirements, Including the Use of Painless to Modify Documents


# Indexing documents in bulk
A good place to start is with batches of 1,000 to 5,000 documents and a total payload between 5MB and 15MB. From there, you can experiment to find the sweet spot.