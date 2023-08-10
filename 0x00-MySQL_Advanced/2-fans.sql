--  A SQL script that ranks country origins of bands, ordered by the number of (non-unique) fan

SELECT origin, SUM(nb_fans) AS total
FROM metal_bands
GROUP BY origin
ORDER BY total DESC;
