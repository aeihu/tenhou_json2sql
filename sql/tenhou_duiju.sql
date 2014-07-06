create table tenhou_duiju
(
	id TEXT PRIMARY KEY,
	ver TEXT,
	ratingc TEXT,
	rule_disp TEXT,
	rule_aka51 INTEGER,
	rule_aka52 INTEGER,
	rule_aka53 INTEGER,
	lobby INTEGER,
	games INTEGER,
	p1_name TEXT,
	p1_sx char(1),
	p1_dan TEXT,
	p1_rate REAL ,
	p1_sc INTEGER,
	p1_pt INTEGER,
	
	p2_name TEXT,
	p2_sx char(1),
	p2_dan TEXT,
	p2_rate REAL ,
	p2_sc INTEGER,
	p2_pt INTEGER,
	
	p3_name TEXT,
	p3_sx char(1),
	p3_dan TEXT,
	p3_rate REAL ,
	p3_sc INTEGER,
	p3_pt INTEGER,
	
	p4_name TEXT,
	p4_sx char(1),
	p4_dan TEXT,
	p4_rate REAL ,
	p4_sc INTEGER,
	p4_pt INTEGER
)