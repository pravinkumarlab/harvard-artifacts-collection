QUERIES = {
"1. 11th Century Byzantine": "SELECT * FROM artifact_metadata WHERE century LIKE '%11%' AND culture='Byzantine'",
"2. Unique Cultures": "SELECT DISTINCT culture FROM artifact_metadata",
"3. Archaic Period": "SELECT * FROM artifact_metadata WHERE period='Archaic'",
"4. Titles by Accession": "SELECT title FROM artifact_metadata ORDER BY accessionyear DESC",
"5. Artifacts per Department": "SELECT department, COUNT(*) FROM artifact_metadata GROUP BY department",

"6. More than 1 Image": "SELECT * FROM artifact_media WHERE imagecount>1",
"7. Average Rank": "SELECT AVG(rank) FROM artifact_media",
"8. Color > Media": "SELECT * FROM artifact_media WHERE colorcount > mediacount",
"9. Created 1500-1600": "SELECT * FROM artifact_media WHERE datebegin>=1500 AND dateend<=1600",
"10.No Media": "SELECT COUNT(*) FROM artifact_media WHERE mediacount=0",

"11. Distinct Hues": "SELECT DISTINCT hue FROM artifact_colors",
"12. Top 5 Colors": "SELECT color, COUNT(*) c FROM artifact_colors GROUP BY color ORDER BY c DESC LIMIT 5",
"13. Avg Hue Coverage": "SELECT hue, AVG(percent) FROM artifact_colors GROUP BY hue",
"14. Colors by Object ID": "SELECT * FROM artifact_colors WHERE objectid = {}",
"15. Total Color Rows": "SELECT COUNT(*) FROM artifact_colors",

"16. Byzantine Titles & Hues": "SELECT m.title, c.hue FROM artifact_metadata m JOIN artifact_colors c ON m.id=c.objectid WHERE m.culture='Byzantine'",
"17. Title with Hues": "SELECT m.title, c.hue FROM artifact_metadata m JOIN artifact_colors c ON m.id=c.objectid",
"18. Period Not Null": "SELECT m.title, m.culture, a.rank FROM artifact_metadata m JOIN artifact_media a ON m.id=a.objectid WHERE m.period IS NOT NULL",
"19. Top 10 Grey": "SELECT m.title FROM artifact_metadata m JOIN artifact_colors c ON m.id=c.objectid WHERE c.hue='Grey' LIMIT 10",
"20. Artifacts per Classification": "SELECT m.classification, COUNT(*), AVG(a.mediacount) FROM artifact_metadata m JOIN artifact_media a ON m.id=a.objectid GROUP BY m.classification",

"21. Artifacts per Century": "SELECT century, COUNT(*) FROM artifact_metadata GROUP BY century ORDER BY COUNT(*) DESC",
"22. Top 10 Departments": "SELECT department, COUNT(*) c FROM artifact_metadata GROUP BY department ORDER BY c DESC LIMIT 10",
"23. Most Used Mediums": "SELECT medium, COUNT(*) FROM artifact_metadata GROUP BY medium ORDER BY COUNT(*) DESC LIMIT 10",
"24. Artifacts Without Culture": "SELECT COUNT(*) FROM artifact_metadata WHERE culture IS NULL",
"25. Oldest Artifacts": "SELECT title, datebegin FROM artifact_media ORDER BY datebegin ASC LIMIT 10",

"26. Newest Artifacts": "SELECT title, dateend FROM artifact_media ORDER BY dateend DESC LIMIT 10",
"27. Average Media Count per Classification": "SELECT m.classification, AVG(a.mediacount) FROM artifact_metadata m JOIN artifact_media a ON m.id=a.objectid GROUP BY m.classification",
"28. Artifacts with Maximum Colors": "SELECT objectid, colorcount FROM artifact_media WHERE colorcount = (SELECT MAX(colorcount) FROM artifact_media);",
"29. Top 5 Hues by Average Coverage": "SELECT hue, AVG(percent) FROM artifact_colors GROUP BY hue ORDER BY AVG(percent) DESC LIMIT 5"
}
