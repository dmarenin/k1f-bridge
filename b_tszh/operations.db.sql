BEGIN TRANSACTION;
CREATE TABLE "operations" (
	`source_data`	TEXT NOT NULL,
	`fisc_reg_data`	TEXT,
	`last_id`	INTEGER,
	`fisc_reg_doc`	INTEGER
);
INSERT INTO `operations` VALUES ('',NULL,1235,NULL);
INSERT INTO `operations` VALUES ('{"result": 0, "description": "\u0423\u0441\u043f\u0435\u0448\u043d\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", "shiftNum": 125, "checkNum": 18, "fiscalDocNum": 1173, "fiscalSign": "1189046352", "checkUrl": "nalog.ru", "changeSum": 4000}','{"ID": 1236, "LID": "s1", "PAYED": "N", "DATE_PAYED": null, "EMP_PAYED_ID": null, "SUMM": 12848.03, "SUMM_PAYED": 0.0, "CURRENCY": "RUB", "USER_ID": 128, "PAY_SYSTEM_ID": 2, "DATE_INSERT": "2018-06-30T09:26:37", ...88", "LANGUAGE_ID": null}',1236,1173);
INSERT INTO `operations` VALUES ('{"result": 0, "description": "\u0423\u0441\u043f\u0435\u0448\u043d\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", "shiftNum": 125, "checkNum": 18, "fiscalDocNum": 1173, "fiscalSign": "1189046352", "checkUrl": "nalog.ru", "changeSum": 4000}','{"ID": 1237, "LID": "s1", "PAYED": "N", "DATE_PAYED": null, "EMP_PAYED_ID": null, "SUMM": 12848.03, "SUMM_PAYED": 0.0, "CURRENCY": "RUB", "USER_ID": 128, "PAY_SYSTEM_ID": 2, "DATE_INSERT": "2018-06-30T09:26:46", "DATE_UPDATE": "2018-06-30T09:26:...4c\u0435\u0432\u0438\u0447", "CONFIRM_CODE": null, "LOGIN_ATTEMPTS": 0, "LAST_ACTIVITY_DATE": null, "AUTO_TIME_ZONE": null, "TIME_ZONE": null, "TIME_ZONE_OFFSET": 0, "TITLE": null, "BX_USER_ID": "aa51cf01e427ee3481364316b2f89088", "LANGUAGE_ID": null}',1237,1173);
INSERT INTO `operations` VALUES ('{"result": 0, "description": "\u0423\u0441\u043f\u0435\u0448\u043d\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", "shiftNum": 125, "checkNum": 18, "fiscalDocNum": 1173, "fiscalSign": "1189046352", "checkUrl": "nalog.ru", "changeSum": 4000}','{"ID": 1238, "LID": "s1", "PAYED": "N", "DATE_PAYED": null, "EMP_PAYED_ID": null, "SUMM": 12848.03, "SUMM_PAYED": 0.0, "CURRENCY": "RUB", "USER_ID": 128, "PAY_SYSTEM_ID": 2, "DATE_INSERT": "2018-06-30T09:34:38", "DATE_U...LANGUAGE_ID": null}',1238,1173);
CREATE INDEX `idx_last_id` ON `operations` (`last_id` DESC)

;
COMMIT;
