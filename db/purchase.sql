CREATE TABLE purchase(
	uid VARCHAR(50) NOT NULL,
	last_viewed_at TIMESTAMP NOT NULL,
	bought_at TIMESTAMP NOT NULL,
	pid VARCHAR(40) NOT NULL REFERENCES product(pid),
	time_interval INTERVAL NOT NULL,
	PRIMARY KEY (uid, bought_at, pid)
);

CREATE INDEX purchase_uid_bought_at_pid_idx ON purchase (uid, bought_at, pid);

ALTER TABLE purchase OWNER TO luiza_labs;

VACUUM ANALYZE purchase;  

ALTER TABLE purchase  
SET (autovacuum_vacuum_scale_factor = 0.0);
 
ALTER TABLE purchase  
SET (autovacuum_vacuum_threshold = 2000);
 
ALTER TABLE purchase  
SET (autovacuum_analyze_scale_factor = 0.0);
 
ALTER TABLE purchase  
SET (autovacuum_analyze_threshold = 2000); 

