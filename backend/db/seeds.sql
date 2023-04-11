-- add users
INSERT INTO users (name) VALUES ("demo1"), ("demo2");

-- add project_types
INSERT INTO project_types (name) VALUES ("tagging"), ("classification");

-- add projects
INSERT INTO projects (project_type_id, name) VALUES (1, "demo_project1"), (1, "demo_project2");
