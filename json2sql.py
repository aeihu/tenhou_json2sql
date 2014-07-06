import sys
import codecs
import json

def tenhou_func(tab, index):
	if index < len(tab):
		return tab[index]
	else:
		return''

def tenhou_json2sql (filename):
	f = codecs.open(filename,"r","utf-8")
	json_obj = json.load(f)
	f.close()

	f = codecs.open("tenhou_duiju_"+json_obj["ref"]+".sql","w","utf-8")
	f.write(str.format('INSERT INTO tenhou_duiju(id, ver, ratingc, rule_disp, rule_aka51, rule_aka52, rule_aka53, lobby, games, '+
		'p1_name, p1_sx, p1_dan, p1_rate, p1_sc, p1_pt,'+
		'p2_name, p2_sx, p2_dan, p2_rate, p2_sc, p2_pt,'+
		'p3_name, p3_sx, p3_dan, p3_rate, p3_sc, p3_pt,'+
		'p4_name, p4_sx, p4_dan, p4_rate, p4_sc, p4_pt'+
		') VALUES ('+
		'"%s", "%s", "%s", "%s", %d, %d, %d, %d, %d, "%s", "%s", "%s", %s, %s, %s, "%s", "%s", "%s", %s, %s, %s, "%s", "%s", "%s", %s, %s, %s, "%s", "%s", "%s", %s, %s, %s)'
		%(
		json_obj["ref"],json_obj["ver"],json_obj["ratingc"],json_obj["rule"]["disp"],
		json_obj["rule"]["aka51"],json_obj["rule"]["aka52"],json_obj["rule"]["aka53"],json_obj["lobby"],len(json_obj["log"]),
		json_obj["name"][0],json_obj["sx"][0],json_obj["dan"][0],json_obj["rate"][0],json_obj["sc"][0],json_obj["sc"][1],
		json_obj["name"][1],json_obj["sx"][1],json_obj["dan"][1],json_obj["rate"][1],json_obj["sc"][2],json_obj["sc"][3],
		json_obj["name"][2],json_obj["sx"][2],json_obj["dan"][2],json_obj["rate"][2],json_obj["sc"][4],json_obj["sc"][5],
		json_obj["name"][3],json_obj["sx"][3],json_obj["dan"][3],json_obj["rate"][3],json_obj["sc"][6],json_obj["sc"][7]
		)))

	for i in range(0, len(json_obj["log"])):
		f.write(str.format(';\nINSERT INTO tenhou_paipu('
			+'log_id, '
			+'turn, '
			+'res, '
			+'houba, '
			+'riiqi, '
			+'p1_sc, '
			+'p1_hk, '
			+'p2_sc, '
			+'p2_hk, '
			+'p3_sc, '
			+'p3_hk, '
			+'p4_sc, '
			+'p4_hk, '
			+'yaku, '
			+'dora, '
			+'u_dora, '
			+'p1_th, '
			+'p2_th, '
			+'p3_th, '
			+'p4_th, '
			+'p1_tm, '
			+'p1_tm1, '
			+'p1_tm2, '
			+'p1_tm3, '
			+'p1_tm4, '
			+'p1_tm5, '
			+'p1_tm6, '
			+'p1_tm7, '
			+'p1_tm8, '
			+'p1_tm9, '
			+'p1_tm10, '
			+'p1_tm11, '
			+'p1_tm12, '
			+'p1_tm13, '
			+'p1_tm14, '
			+'p1_tm15, '
			+'p1_tm16, '
			+'p1_tm17, '
			+'p1_tm18, '
			+'p1_tm19, '
			+'p1_tm20, '
			+'p1_tm21, '
			+'p1_tm22, '
			+'p1_kr, '
			+'p1_kr1, '
			+'p1_kr2, '
			+'p1_kr3, '
			+'p1_kr4, '
			+'p1_kr5, '
			+'p1_kr6, '
			+'p1_kr7, '
			+'p1_kr8, '
			+'p1_kr9, '
			+'p1_kr10, '
			+'p1_kr11, '
			+'p1_kr12, '
			+'p1_kr13, '
			+'p1_kr14, '
			+'p1_kr15, '
			+'p1_kr16, '
			+'p1_kr17, '
			+'p1_kr18, '
			+'p1_kr19, '
			+'p1_kr20, '
			+'p1_kr21, '
			+'p1_kr22, '
			+'p2_tm, '
			+'p2_tm1, '
			+'p2_tm2, '
			+'p2_tm3, '
			+'p2_tm4, '
			+'p2_tm5, '
			+'p2_tm6, '
			+'p2_tm7, '
			+'p2_tm8, '
			+'p2_tm9, '
			+'p2_tm10, '
			+'p2_tm11, '
			+'p2_tm12, '
			+'p2_tm13, '
			+'p2_tm14, '
			+'p2_tm15, '
			+'p2_tm16, '
			+'p2_tm17, '
			+'p2_tm18, '
			+'p2_tm19, '
			+'p2_tm20, '
			+'p2_tm21, '
			+'p2_tm22, '
			+'p2_kr, '
			+'p2_kr1, '
			+'p2_kr2, '
			+'p2_kr3, '
			+'p2_kr4, '
			+'p2_kr5, '
			+'p2_kr6, '
			+'p2_kr7, '
			+'p2_kr8, '
			+'p2_kr9, '
			+'p2_kr10, '
			+'p2_kr11, '
			+'p2_kr12, '
			+'p2_kr13, '
			+'p2_kr14, '
			+'p2_kr15, '
			+'p2_kr16, '
			+'p2_kr17, '
			+'p2_kr18, '
			+'p2_kr19, '
			+'p2_kr20, '
			+'p2_kr21, '
			+'p2_kr22, '
			+'p3_tm, '
			+'p3_tm1, '
			+'p3_tm2, '
			+'p3_tm3, '
			+'p3_tm4, '
			+'p3_tm5, '
			+'p3_tm6, '
			+'p3_tm7, '
			+'p3_tm8, '
			+'p3_tm9, '
			+'p3_tm10, '
			+'p3_tm11, '
			+'p3_tm12, '
			+'p3_tm13, '
			+'p3_tm14, '
			+'p3_tm15, '
			+'p3_tm16, '
			+'p3_tm17, '
			+'p3_tm18, '
			+'p3_tm19, '
			+'p3_tm20, '
			+'p3_tm21, '
			+'p3_tm22, '
			+'p3_kr, '
			+'p3_kr1, '
			+'p3_kr2, '
			+'p3_kr3, '
			+'p3_kr4, '
			+'p3_kr5, '
			+'p3_kr6, '
			+'p3_kr7, '
			+'p3_kr8, '
			+'p3_kr9, '
			+'p3_kr10, '
			+'p3_kr11, '
			+'p3_kr12, '
			+'p3_kr13, '
			+'p3_kr14, '
			+'p3_kr15, '
			+'p3_kr16, '
			+'p3_kr17, '
			+'p3_kr18, '
			+'p3_kr19, '
			+'p3_kr20, '
			+'p3_kr21, '
			+'p3_kr22, '
			+'p4_tm, '
			+'p4_tm1, '
			+'p4_tm2, '
			+'p4_tm3, '
			+'p4_tm4, '
			+'p4_tm5, '
			+'p4_tm6, '
			+'p4_tm7, '
			+'p4_tm8, '
			+'p4_tm9, '
			+'p4_tm10, '
			+'p4_tm11, '
			+'p4_tm12, '
			+'p4_tm13, '
			+'p4_tm14, '
			+'p4_tm15, '
			+'p4_tm16, '
			+'p4_tm17, '
			+'p4_tm18, '
			+'p4_tm19, '
			+'p4_tm20, '
			+'p4_tm21, '
			+'p4_tm22, '
			+'p4_kr, '
			+'p4_kr1, '
			+'p4_kr2, '
			+'p4_kr3, '
			+'p4_kr4, '
			+'p4_kr5, '
			+'p4_kr6, '
			+'p4_kr7, '
			+'p4_kr8, '
			+'p4_kr9, '
			+'p4_kr10, '
			+'p4_kr11, '
			+'p4_kr12, '
			+'p4_kr13, '
			+'p4_kr14, '
			+'p4_kr15, '
			+'p4_kr16, '
			+'p4_kr17, '
			+'p4_kr18, '
			+'p4_kr19, '
			+'p4_kr20, '
			+'p4_kr21, '
			+'p4_kr22) VALUES ('
			+'"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
			%(json_obj["ref"],json_obj["log"][i][0][0],json_obj["log"][i][16][0],json_obj["log"][i][0][1],json_obj["log"][i][0][2],
				json_obj["log"][i][1][0],json_obj["log"][i][16][1][0],
				json_obj["log"][i][1][1],json_obj["log"][i][16][1][1],
				json_obj["log"][i][1][2],json_obj["log"][i][16][1][2],
				json_obj["log"][i][1][3],json_obj["log"][i][16][1][3],
				tenhou_func(json_obj["log"][i][16], 2),
				json_obj["log"][i][2],json_obj["log"][i][3],
				json_obj["log"][i][4],json_obj["log"][i][7],json_obj["log"][i][10],json_obj["log"][i][13],
				#p1
				json_obj["log"][i][5],
				tenhou_func(json_obj["log"][i][5], 0),
				tenhou_func(json_obj["log"][i][5], 1),
				tenhou_func(json_obj["log"][i][5], 2),
				tenhou_func(json_obj["log"][i][5], 3),
				tenhou_func(json_obj["log"][i][5], 4),
				tenhou_func(json_obj["log"][i][5], 5),
				tenhou_func(json_obj["log"][i][5], 6),
				tenhou_func(json_obj["log"][i][5], 7),
				tenhou_func(json_obj["log"][i][5], 8),
				tenhou_func(json_obj["log"][i][5], 9),
				tenhou_func(json_obj["log"][i][5], 10),
				tenhou_func(json_obj["log"][i][5], 11),
				tenhou_func(json_obj["log"][i][5], 12),
				tenhou_func(json_obj["log"][i][5], 13),
				tenhou_func(json_obj["log"][i][5], 14),
				tenhou_func(json_obj["log"][i][5], 15),
				tenhou_func(json_obj["log"][i][5], 16),
				tenhou_func(json_obj["log"][i][5], 17),
				tenhou_func(json_obj["log"][i][5], 18),
				tenhou_func(json_obj["log"][i][5], 19),
				tenhou_func(json_obj["log"][i][5], 20),
				tenhou_func(json_obj["log"][i][5], 21),
				json_obj["log"][i][6],
				tenhou_func(json_obj["log"][i][6], 0),
				tenhou_func(json_obj["log"][i][6], 1),
				tenhou_func(json_obj["log"][i][6], 2),
				tenhou_func(json_obj["log"][i][6], 3),
				tenhou_func(json_obj["log"][i][6], 4),
				tenhou_func(json_obj["log"][i][6], 5),
				tenhou_func(json_obj["log"][i][6], 6),
				tenhou_func(json_obj["log"][i][6], 7),
				tenhou_func(json_obj["log"][i][6], 8),
				tenhou_func(json_obj["log"][i][6], 9),
				tenhou_func(json_obj["log"][i][6], 10),
				tenhou_func(json_obj["log"][i][6], 11),
				tenhou_func(json_obj["log"][i][6], 12),
				tenhou_func(json_obj["log"][i][6], 13),
				tenhou_func(json_obj["log"][i][6], 14),
				tenhou_func(json_obj["log"][i][6], 15),
				tenhou_func(json_obj["log"][i][6], 16),
				tenhou_func(json_obj["log"][i][6], 17),
				tenhou_func(json_obj["log"][i][6], 18),
				tenhou_func(json_obj["log"][i][6], 19),
				tenhou_func(json_obj["log"][i][6], 20),
				tenhou_func(json_obj["log"][i][6], 21),
				#p2
				json_obj["log"][i][8],
				tenhou_func(json_obj["log"][i][8], 0),
				tenhou_func(json_obj["log"][i][8], 1),
				tenhou_func(json_obj["log"][i][8], 2),
				tenhou_func(json_obj["log"][i][8], 3),
				tenhou_func(json_obj["log"][i][8], 4),
				tenhou_func(json_obj["log"][i][8], 5),
				tenhou_func(json_obj["log"][i][8], 6),
				tenhou_func(json_obj["log"][i][8], 7),
				tenhou_func(json_obj["log"][i][8], 8),
				tenhou_func(json_obj["log"][i][8], 9),
				tenhou_func(json_obj["log"][i][8], 10),
				tenhou_func(json_obj["log"][i][8], 11),
				tenhou_func(json_obj["log"][i][8], 12),
				tenhou_func(json_obj["log"][i][8], 13),
				tenhou_func(json_obj["log"][i][8], 14),
				tenhou_func(json_obj["log"][i][8], 15),
				tenhou_func(json_obj["log"][i][8], 16),
				tenhou_func(json_obj["log"][i][8], 17),
				tenhou_func(json_obj["log"][i][8], 18),
				tenhou_func(json_obj["log"][i][8], 19),
				tenhou_func(json_obj["log"][i][8], 20),
				tenhou_func(json_obj["log"][i][8], 21),
				json_obj["log"][i][9],			
				tenhou_func(json_obj["log"][i][9], 0),
				tenhou_func(json_obj["log"][i][9], 1),
				tenhou_func(json_obj["log"][i][9], 2),
				tenhou_func(json_obj["log"][i][9], 3),
				tenhou_func(json_obj["log"][i][9], 4),
				tenhou_func(json_obj["log"][i][9], 5),
				tenhou_func(json_obj["log"][i][9], 6),
				tenhou_func(json_obj["log"][i][9], 7),
				tenhou_func(json_obj["log"][i][9], 8),
				tenhou_func(json_obj["log"][i][9], 9),
				tenhou_func(json_obj["log"][i][9], 10),
				tenhou_func(json_obj["log"][i][9], 11),
				tenhou_func(json_obj["log"][i][9], 12),
				tenhou_func(json_obj["log"][i][9], 13),
				tenhou_func(json_obj["log"][i][9], 14),
				tenhou_func(json_obj["log"][i][9], 15),
				tenhou_func(json_obj["log"][i][9], 16),
				tenhou_func(json_obj["log"][i][9], 17),
				tenhou_func(json_obj["log"][i][9], 18),
				tenhou_func(json_obj["log"][i][9], 19),
				tenhou_func(json_obj["log"][i][9], 20),
				tenhou_func(json_obj["log"][i][9], 21),
				#p3
				json_obj["log"][i][11],
				tenhou_func(json_obj["log"][i][11], 0),
				tenhou_func(json_obj["log"][i][11], 1),
				tenhou_func(json_obj["log"][i][11], 2),
				tenhou_func(json_obj["log"][i][11], 3),
				tenhou_func(json_obj["log"][i][11], 4),
				tenhou_func(json_obj["log"][i][11], 5),
				tenhou_func(json_obj["log"][i][11], 6),
				tenhou_func(json_obj["log"][i][11], 7),
				tenhou_func(json_obj["log"][i][11], 8),
				tenhou_func(json_obj["log"][i][11], 9),
				tenhou_func(json_obj["log"][i][11], 10),
				tenhou_func(json_obj["log"][i][11], 11),
				tenhou_func(json_obj["log"][i][11], 12),
				tenhou_func(json_obj["log"][i][11], 13),
				tenhou_func(json_obj["log"][i][11], 14),
				tenhou_func(json_obj["log"][i][11], 15),
				tenhou_func(json_obj["log"][i][11], 16),
				tenhou_func(json_obj["log"][i][11], 17),
				tenhou_func(json_obj["log"][i][11], 18),
				tenhou_func(json_obj["log"][i][11], 19),
				tenhou_func(json_obj["log"][i][11], 20),
				tenhou_func(json_obj["log"][i][11], 21),
				json_obj["log"][i][12],			
				tenhou_func(json_obj["log"][i][12], 0),
				tenhou_func(json_obj["log"][i][12], 1),
				tenhou_func(json_obj["log"][i][12], 2),
				tenhou_func(json_obj["log"][i][12], 3),
				tenhou_func(json_obj["log"][i][12], 4),
				tenhou_func(json_obj["log"][i][12], 5),
				tenhou_func(json_obj["log"][i][12], 6),
				tenhou_func(json_obj["log"][i][12], 7),
				tenhou_func(json_obj["log"][i][12], 8),
				tenhou_func(json_obj["log"][i][12], 9),
				tenhou_func(json_obj["log"][i][12], 10),
				tenhou_func(json_obj["log"][i][12], 11),
				tenhou_func(json_obj["log"][i][12], 12),
				tenhou_func(json_obj["log"][i][12], 13),
				tenhou_func(json_obj["log"][i][12], 14),
				tenhou_func(json_obj["log"][i][12], 15),
				tenhou_func(json_obj["log"][i][12], 16),
				tenhou_func(json_obj["log"][i][12], 17),
				tenhou_func(json_obj["log"][i][12], 18),
				tenhou_func(json_obj["log"][i][12], 19),
				tenhou_func(json_obj["log"][i][12], 20),
				tenhou_func(json_obj["log"][i][12], 21),
				#p4
				json_obj["log"][i][14],			
				tenhou_func(json_obj["log"][i][14], 0),
				tenhou_func(json_obj["log"][i][14], 1),
				tenhou_func(json_obj["log"][i][14], 2),
				tenhou_func(json_obj["log"][i][14], 3),
				tenhou_func(json_obj["log"][i][14], 4),
				tenhou_func(json_obj["log"][i][14], 5),
				tenhou_func(json_obj["log"][i][14], 6),
				tenhou_func(json_obj["log"][i][14], 7),
				tenhou_func(json_obj["log"][i][14], 8),
				tenhou_func(json_obj["log"][i][14], 9),
				tenhou_func(json_obj["log"][i][14], 10),
				tenhou_func(json_obj["log"][i][14], 11),
				tenhou_func(json_obj["log"][i][14], 12),
				tenhou_func(json_obj["log"][i][14], 13),
				tenhou_func(json_obj["log"][i][14], 14),
				tenhou_func(json_obj["log"][i][14], 15),
				tenhou_func(json_obj["log"][i][14], 16),
				tenhou_func(json_obj["log"][i][14], 17),
				tenhou_func(json_obj["log"][i][14], 18),
				tenhou_func(json_obj["log"][i][14], 19),
				tenhou_func(json_obj["log"][i][14], 20),
				tenhou_func(json_obj["log"][i][14], 21),
				json_obj["log"][i][15],			
				tenhou_func(json_obj["log"][i][15], 0),
				tenhou_func(json_obj["log"][i][15], 1),
				tenhou_func(json_obj["log"][i][15], 2),
				tenhou_func(json_obj["log"][i][15], 3),
				tenhou_func(json_obj["log"][i][15], 4),
				tenhou_func(json_obj["log"][i][15], 5),
				tenhou_func(json_obj["log"][i][15], 6),
				tenhou_func(json_obj["log"][i][15], 7),
				tenhou_func(json_obj["log"][i][15], 8),
				tenhou_func(json_obj["log"][i][15], 9),
				tenhou_func(json_obj["log"][i][15], 10),
				tenhou_func(json_obj["log"][i][15], 11),
				tenhou_func(json_obj["log"][i][15], 12),
				tenhou_func(json_obj["log"][i][15], 13),
				tenhou_func(json_obj["log"][i][15], 14),
				tenhou_func(json_obj["log"][i][15], 15),
				tenhou_func(json_obj["log"][i][15], 16),
				tenhou_func(json_obj["log"][i][15], 17),
				tenhou_func(json_obj["log"][i][15], 18),
				tenhou_func(json_obj["log"][i][15], 19),
				tenhou_func(json_obj["log"][i][15], 20),
				tenhou_func(json_obj["log"][i][15], 21)
				)
		))
		
	f.close()
	
tenhou_json2sql(sys.argv[1])