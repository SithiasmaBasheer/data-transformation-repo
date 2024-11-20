MERGE INTO customer_increamental AS target
USING customer_stage AS source
ON target.C_CUSTOMER_ID = source.C_CUSTOMER_ID
   AND target.IS_CURRENT = TRUE
WHEN MATCHED AND (
    -- sample fields for checking updates, it will be based on business requirement
       target.C_BIRTH_COUNTRY != source.C_BIRTH_COUNTRY
    OR target.C_EMAIL_DOMAIN != source.C_EMAIL_DOMAIN
    OR target.C_PREFERRED_CUST_FLAG != source.C_PREFERRED_CUST_FLAG
) THEN
    -- Update old record to mark it as historical
    UPDATE SET 
        RECORD_VALID_TO = CURRENT_TIMESTAMP,
        IS_CURRENT = FALSE
WHEN NOT MATCHED THEN
    -- Insert new record
    INSERT (
        C_CUSTOMER_ID, C_CUSTOMER_SK, C_BIRTH_COUNTRY, C_BIRTH_DAY, C_BIRTH_MONTH, 
        C_BIRTH_YEAR, C_CURRENT_ADDR_SK, C_CURRENT_CDEMO_SK, C_CURRENT_HDEMO_SK, 
        C_FIRST_SALES_DATE_SK, C_FIRST_SHIPTO_DATE_SK, C_LAST_REVIEW_DATE, 
        C_PREFERRED_CUST_FLAG, C_SALUTATION, C_EMAIL_DOMAIN, 
        LOAD_TIMESTAMP, RECORD_VALID_FROM, IS_CURRENT
    )
    VALUES (
        source.C_CUSTOMER_ID, source.C_CUSTOMER_SK, source.C_BIRTH_COUNTRY, source.C_BIRTH_DAY, source.C_BIRTH_MONTH, 
        source.C_BIRTH_YEAR, source.C_CURRENT_ADDR_SK, source.C_CURRENT_CDEMO_SK, source.C_CURRENT_HDEMO_SK, 
        source.C_FIRST_SALES_DATE_SK, source.C_FIRST_SHIPTO_DATE_SK, source.C_LAST_REVIEW_DATE, 
        source.C_PREFERRED_CUST_FLAG, source.C_SALUTATION, source.C_EMAIL_DOMAIN, 
        CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, TRUE
    );


