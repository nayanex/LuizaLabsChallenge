CREATE TABLE interaction(
	uid VARCHAR(50) NOT NULL,
	pid VARCHAR(40) NOT NULL REFERENCES product(pid),
	action VARCHAR(20) NOT NULL,
	channel VARCHAR(25) NOT NULL,
	price_at DOUBLE PRECISION,
	at TIMESTAMP NOT NULL,
	UNIQUE (uid, pid, action, channel, at)
);


ALTER TABLE user_interaction OWNER TO luiza_labs;

VACUUM ANALYZE user_interaction;  

ALTER TABLE user_interaction  
SET (autovacuum_vacuum_scale_factor = 0.0);
 
ALTER TABLE user_interaction  
SET (autovacuum_vacuum_threshold = 5000);
 
ALTER TABLE user_interaction  
SET (autovacuum_analyze_scale_factor = 0.0);
 
ALTER TABLE user_interaction  
SET (autovacuum_analyze_threshold = 5000); 


