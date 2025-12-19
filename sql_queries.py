QUERIES = {

# ───── artifact_metadata ─────
"1. 11th Century Byzantine":
"SELECT * FROM artifact_metadata WHERE century LIKE '%11%' AND culture = 'Byzantine'",

"2. Unique Cultures":
"SELECT DISTINCT culture FROM artifact_metadata",

"3. Archaic Period":
"SELECT * FROM artifact_metadata WHERE period = 'Archaic'",

"4. Titles by Accession Year":
"SELECT title FROM artifact_metadata ORDER BY accessionyear DESC",

"5. Artifacts per Department":
"SELECT department, COUNT(*) AS total FROM artifact_metadata GROUP BY department",

# ───── artifact_media ─────
"6. More than 1 Image":
"SELECT * FROM artifact_media WHERE imagecount > 1",

"7. Average Rank":
"SELECT AVG(rank) AS avg_rank FROM artifact_media",

"8. Colorcount > Mediacount":
"SELECT * FROM artifact_media WHERE colorcount > mediacount",

"9. Created Between 1500 and 1600":
"SELECT * FROM artifact_media WHERE datebegin >= 1500 AND dateend <= 1600",

"10. No Media Files":
"SELECT COUNT(*) AS no_media FROM artifact_media WHERE mediacount = 0",

# ───── artifact_colors ─────
"11. Distinct Hues":
"SELECT DISTINCT hue FROM artifact_colors",

"12. Top 5 Colors":
"SELECT color, COUNT(*) AS frequency FROM artifact_colors GROUP BY color ORDER BY frequency DESC LIMIT 5",

"13. Average Hue Coverage":
"SELECT hue, AVG(percent) AS avg_coverage FROM artifact_colors GROUP BY hue",

"14. Colors by Object ID":
"SELECT * FROM artifact_colors WHERE objectid = {}",

"15. Total Color Rows":
"SELECT COUNT(*) AS total_rows FROM artifact_colors",

# ───── Join Queries ─────
"16. Byzantine Titles & Hues":
"""SELECT m.title, c.hue
   FROM artifact_metadata m
   JOIN artifact_colors c ON m.id = c.objectid
   WHERE m.culture = 'Byzantine'""",

"17. Title with Hues":
"""SELECT m.title, c.hue
   FROM artifact_metadata m
   JOIN artifact_colors c ON m.id = c.objectid""",

"18. Period Not Null":
"""SELECT m.title, m.culture, a.rank
   FROM artifact_metadata m
   JOIN artifact_media a ON m.id = a.objectid
   WHERE m.period IS NOT NULL""",

"19. Top 10 Grey Artifacts":
"""SELECT DISTINCT m.title
   FROM artifact_metadata m
   JOIN artifact_colors c ON m.id = c.objectid
   WHERE c.hue = 'Grey'
   LIMIT 10""",

"20. Artifacts per Classification":
"""SELECT m.classification,
          COUNT(*) AS total_artifacts,
          AVG(a.mediacount) AS avg_media
   FROM artifact_metadata m
   JOIN artifact_media a ON m.id = a.objectid
   GROUP BY m.classification""",

# ───── Additional Learner Queries ─────
"21. Artifacts per Century":
"SELECT century, COUNT(*) AS total_artifacts FROM artifact_metadata GROUP BY century ORDER BY total_artifacts DESC",

"22. Top 10 Departments":
"SELECT department, COUNT(*) AS total FROM artifact_metadata GROUP BY department ORDER BY total DESC LIMIT 10",

"23. Most Used Mediums":
"SELECT medium, COUNT(*) AS total FROM artifact_metadata GROUP BY medium ORDER BY total DESC LIMIT 10",

"24. Missing Culture Count":
"SELECT COUNT(*) AS missing_culture FROM artifact_metadata WHERE culture IS NULL",

"25. Oldest Artifacts":
"""SELECT m.title, a.datebegin
   FROM artifact_metadata m
   JOIN artifact_media a ON m.id = a.objectid
   WHERE a.datebegin IS NOT NULL
   ORDER BY a.datebegin ASC
   LIMIT 10""",

"26. Newest Artifacts":
"""SELECT m.title, a.dateend
   FROM artifact_metadata m
   JOIN artifact_media a ON m.id = a.objectid
   WHERE a.dateend IS NOT NULL
   ORDER BY a.dateend DESC
   LIMIT 10""",

"27. Avg Media per Classification":
"""SELECT m.classification, AVG(a.mediacount) AS avg_media
   FROM artifact_metadata m
   JOIN artifact_media a ON m.id = a.objectid
   GROUP BY m.classification""",

"28. Max Color Artifacts":
"""SELECT objectid, colorcount
   FROM artifact_media
   WHERE colorcount = (SELECT MAX(colorcount) FROM artifact_media)""",

"29. Top 5 Hues by Coverage":
"""SELECT hue, AVG(percent) AS avg_coverage
   FROM artifact_colors
   GROUP BY hue
   ORDER BY avg_coverage DESC
   LIMIT 5""",

"30. Total Artifacts Collected":
"SELECT COUNT(*) AS total_artifacts FROM artifact_metadata"
}
