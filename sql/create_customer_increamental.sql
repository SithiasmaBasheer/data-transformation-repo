CREATE TABLE customer_increamental (
    C_CUSTOMER_ID VARCHAR,         -- Primary Identifier
    C_CUSTOMER_SK INT,
    C_BIRTH_COUNTRY VARCHAR,
    C_BIRTH_DAY INT,
    C_BIRTH_MONTH INT,
    C_BIRTH_YEAR INT,
    C_CURRENT_ADDR_SK INT,
    C_CURRENT_CDEMO_SK INT,
    C_CURRENT_HDEMO_SK INT,
    C_FIRST_SALES_DATE_SK INT,
    C_FIRST_SHIPTO_DATE_SK INT,
    C_LAST_REVIEW_DATE INT,
    C_PREFERRED_CUST_FLAG VARCHAR,
    C_SALUTATION VARCHAR,
    C_EMAIL_DOMAIN VARCHAR,        -- New field
    LOAD_TIMESTAMP TIMESTAMP,      -- When the record was loaded
    RECORD_VALID_FROM TIMESTAMP,   -- Start of record validity
    RECORD_VALID_TO TIMESTAMP,     -- End of record validity (null for current record)
    IS_CURRENT BOOLEAN             -- Flag for current record
);
