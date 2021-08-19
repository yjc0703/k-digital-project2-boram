CREATE TABLE respondent
(
    `ID`   INT    NOT NULL    COMMENT '응답자 일련번호', 
    `DM1`  INT    NULL        COMMENT '대상구분', 
    `DM2`  INT    NULL        COMMENT '성별', 
    CONSTRAINT PK_ PRIMARY KEY (ID)
);

ALTER TABLE respondent COMMENT '응답자';



CREATE TABLE response_yjc
(
    `ID`     INT    NOT NULL    COMMENT '응답자 일련번호', 
    `Q12`    INT    NULL        COMMENT '질문12', 
    `Q12_1`  INT    NULL        COMMENT '질문12_1', 
     PRIMARY KEY (ID)
);

ALTER TABLE response_yjc COMMENT '응답_시각화_윤재철';

ALTER TABLE response_yjc
    ADD CONSTRAINT FK_response_yjc_ID_respondent_ID FOREIGN KEY (ID)
        REFERENCES respondent (ID) ON DELETE RESTRICT ON UPDATE RESTRICT;
        
       
       
CREATE TABLE response_kay
(
    `ID`   INT    NOT NULL    COMMENT '응답자 일련번호', 
    `Q9A`  INT    NULL        COMMENT '질문9', 
    `Q10`  INT    NULL        COMMENT '질문10', 
     PRIMARY KEY (ID)
);

ALTER TABLE response_kay COMMENT '응답_시각화_김아영';

ALTER TABLE response_kay
    ADD CONSTRAINT FK_response_kay_ID_respondent_ID FOREIGN KEY (ID)
        REFERENCES respondent (ID) ON DELETE RESTRICT ON UPDATE RESTRICT;
        
       
       
CREATE TABLE response_kym
(
    `ID`      INT    NOT NULL    COMMENT '응답자 일련번호', 
    `Q8`      INT    NULL        COMMENT '질문8', 
    `Q8_1_1`  INT    NULL        COMMENT '질문8_1', 
    `Q8_1_2`  INT    NULL        COMMENT '질문8_2', 
    `Q8_1_3`  INT    NULL        COMMENT '질문8_3', 
    `Q8_1_4`  INT    NULL        COMMENT '질문8_4', 
    `Q8_1_5`  INT    NULL        COMMENT '질문8_5', 
    `Q8_1_6`  INT    NULL        COMMENT '질문8_6', 
     PRIMARY KEY (ID)
);

ALTER TABLE response_kym COMMENT '응답_시각화_김유민';

ALTER TABLE response_kym
    ADD CONSTRAINT FK_response_kym_ID_respondent_ID FOREIGN KEY (ID)
        REFERENCES respondent (ID) ON DELETE RESTRICT ON UPDATE RESTRICT;
        
       
       
       
CREATE TABLE response_cjy
(
    `ID`      INT    NOT NULL    COMMENT '응답자 일련번호', 
    `Q1A_1`   INT    NULL        COMMENT '질문1A_1', 
    `Q1A_2`   INT    NULL        COMMENT '질문1A_2', 
    `Q1A_3`   INT    NULL        COMMENT '질문1A_3', 
    `Q1A_4`   INT    NULL        COMMENT '질문1A_4', 
    `Q1A_5`   INT    NULL        COMMENT '질문1A_5', 
    `Q1A_6`   INT    NULL        COMMENT '질문1A_6', 
    `Q1A_7`   INT    NULL        COMMENT '질문1A_7', 
    `Q1A_8`   INT    NULL        COMMENT '질문1A_8', 
    `Q1A_9`   INT    NULL        COMMENT '질문1A_9', 
    `Q1A_10`  INT    NULL        COMMENT '질문1A_10', 
    `Q1A_11`  INT    NULL        COMMENT '질문1A_11', 
    `Q1A_12`  INT    NULL        COMMENT '질문1A_12', 
    `Q1A_13`  INT    NULL        COMMENT '질문1A_13', 
    `Q1A_14`  INT    NULL        COMMENT '질문1A_14', 
    `Q1A_15`  INT    NULL        COMMENT '질문1A_15', 
    `Q1A_16`  INT    NULL        COMMENT '질문1A_16', 
    `Q1A_17`  INT    NULL        COMMENT '질문1A_17', 
    `Q1A_18`  INT    NULL        COMMENT '질문1A_18', 
    `Q1A_19`  INT    NULL        COMMENT '질문1A_19', 
    `Q1A_20`  INT    NULL        COMMENT '질문1A_20', 
    `Q4`      INT    NULL        COMMENT '질문4', 
     PRIMARY KEY (ID)
);

ALTER TABLE response_cjy COMMENT '응답_시각화_최진영';

ALTER TABLE response_cjy
    ADD CONSTRAINT FK_response_cjy_ID_respondent_ID FOREIGN KEY (ID)
        REFERENCES respondent (ID) ON DELETE RESTRICT ON UPDATE RESTRICT;
        
       
       
CREATE TABLE response_fit
(
    `ID`     INT    NOT NULL    COMMENT '응답자 일련번호', 
    `Q3_1`   INT    NULL        COMMENT '문항1', 
    `Q3_2`   INT    NULL        COMMENT '문항2', 
    `Q3_3`   INT    NULL        COMMENT '문항3', 
    `Q3_4`   INT    NULL        COMMENT '문항4', 
    `Q3_5`   INT    NULL        COMMENT '문항5', 
    `Q3_6`   INT    NULL        COMMENT '문항6', 
    `Q3_7`   INT    NULL        COMMENT '문항7', 
    `Q3_8`   INT    NULL        COMMENT '문항8', 
    `Q3_9`   INT    NULL        COMMENT '문항9', 
    `Q3_10`  INT    NULL        COMMENT '문항10', 
    `KK1`    INT    NULL        COMMENT '결과', 
    CONSTRAINT PK_ PRIMARY KEY (ID)
);

ALTER TABLE response_fit COMMENT '응답결과';

ALTER TABLE response_fit
    ADD CONSTRAINT FK_response_fit_ID_respondent_ID FOREIGN KEY (ID)
        REFERENCES respondent (ID) ON DELETE RESTRICT ON UPDATE RESTRICT;