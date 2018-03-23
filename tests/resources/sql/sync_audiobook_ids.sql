SELECT setval('audiobooks_id_seq', COALESCE((SELECT MAX(id)+1 FROM audiobooks), 1), false);
