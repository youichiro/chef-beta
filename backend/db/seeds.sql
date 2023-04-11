-- truncate
SET foreign_key_checks = 0;
TRUNCATE TABLE tags;
TRUNCATE TABLE annotations;
TRUNCATE TABLE documents;
TRUNCATE TABLE labels;
TRUNCATE TABLE datasets;
TRUNCATE TABLE guidelines;
TRUNCATE TABLE project_members;
TRUNCATE TABLE projects;
TRUNCATE TABLE project_types;
TRUNCATE TABLE users;
SET foreign_key_checks = 1;

-- add users
INSERT INTO users (name) VALUES ("demo1"), ("demo2");

-- add project_types
INSERT INTO project_types (name) VALUES ("tagging"), ("classification");

-- add projects
INSERT INTO projects (project_type_id, name) VALUES (1, "demo_project1"), (1, "demo_project2");

-- add project_members
INSERT INTO project_members (project_id, member_id) VALUES (1, 1), (1, 2), (2, 1), (2, 2);

-- add guidelines
INSERT INTO guidelines (project_id, content) VALUES (1, "demo_project1 guideline");

-- add datasets
INSERT INTO datasets (project_id, name) VALUES (1, "dataset1"), (1, "dataset2"), (2, "dataset1"), (2, "dataset2");

-- add labels
INSERT INTO labels (dataset_id, name, color) VALUES (1, "name", "blue-500"), (1, "name", "orange-500");

-- add documents
INSERT INTO documents (dataset_id, content) VALUES (1, "私の名前はxxxです"), (1, "私の名前はxxxです 私の名前はxxxです 私の名前はxxxです 私の名前はxxxです");
