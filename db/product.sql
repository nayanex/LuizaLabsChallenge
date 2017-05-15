CREATE TABLE product(
	pid VARCHAR(40) PRIMARY KEY,
	name VARCHAR(250) NOT NULL,
	category VARCHAR(5) NOT NULL,
	department VARCHAR(5) NOT NULL,
	brand VARCHAR(50) NOT NULL,
	rating DOUBLE PRECISION
);

CREATE INDEX product_category_idx ON product (category);
CREATE INDEX product_department_idx ON product (department);
CREATE INDEX product_brand_idx ON product (brand);
CREATE INDEX product_rating_idx ON product (rating);

ALTER TABLE product OWNER TO luiza_labs;

VACUUM ANALYZE product;  

ALTER TABLE product  
SET (autovacuum_vacuum_scale_factor = 0.0);
 
ALTER TABLE product  
SET (autovacuum_vacuum_threshold = 1000);
 
ALTER TABLE product  
SET (autovacuum_analyze_scale_factor = 0.0);
 
ALTER TABLE product  
SET (autovacuum_analyze_threshold = 1000); 

