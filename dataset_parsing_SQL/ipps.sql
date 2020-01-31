-- Database Assignment 02
-- Author(s): John Shapiro

CREATE DATABASE ipps;
USE ipps;

CREATE TABLE DRGs(
    code    CHAR(3) PRIMARY KEY,
    descrip VARCHAR(80) NOT NULL
);

CREATE TABLE Providers(
    id             INT PRIMARY KEY,
    name           VARCHAR(63) NOT NULL, 
    street_address VARCHAR(63) NOT NULL,
    city           VARCHAR(31) NOT NULL,
    state          CHAR(2) NOT NULL,
    zip_code       CHAR(5) NOT NULL,
    hrr_state      CHAR(2) NOT NULL,
    hrr_city       VARCHAR(31) NOT NULL
);

CREATE TABLE DischargeStats(
    drg_code              CHAR(3),
    provider_id           INT,
    discharges            INT NOT NULL,
    avg_covered           DEC(10, 2) NOT NULL,
    avg_total_payments    DEC(10, 2) NOT NULL,
    avg_medicare_payments DEC (10, 2) NOT NULL,
    PRIMARY KEY (drg_code, provider_id),
    FOREIGN KEY (drg_code) REFERENCES DRGs(code),
    FOREIGN KEY (provider_id) REFERENCES Providers(id)
);

CREATE TABLE HRRs(
    state CHAR(2) REFERENCES Providers(hrr_state),
    city  VARCHAR(31) REFERENCES Providers(hrr_city),
    PRIMARY KEY (state, city)
);

CREATE USER 'ipps' IDENTIFIED BY '024680';
GRANT ALL ON TABLE DRGs TO 'ipps';
GRANT ALL ON TABLE Providers TO 'ipps';
GRANT ALL ON TABLE DischargeStats TO 'ipps';
GRANT ALL ON TABLE HRRs TO 'ipps';