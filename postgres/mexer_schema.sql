--
-- PostgreSQL database dump
--

\restrict kM8THnfXpEAyvNuMxOqEMBRJ2dQ0XGrxI5VRx8UJXuWm4OLxe37UNtw17TLD2w5

-- Dumped from database version 16.13 (Ubuntu 16.13-1.pgdg22.04+1)
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: AMWPFUData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."AMWPFUData" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Year" integer NOT NULL,
    "Species" integer NOT NULL,
    "Stage" integer NOT NULL,
    "Sector" integer NOT NULL,
    "Unit" integer NOT NULL,
    "Edot" double precision
);


--
-- Name: AMWPFUDataRaw; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."AMWPFUDataRaw" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Year" integer NOT NULL,
    "Species" integer NOT NULL,
    "Stage" integer NOT NULL,
    "Sector" integer NOT NULL,
    "Unit" integer NOT NULL,
    "Edot" double precision
);


--
-- Name: AggEtaPFU; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."AggEtaPFU" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "IncludesNEU" integer NOT NULL,
    "Year" integer NOT NULL,
    "ChoppedMat" integer NOT NULL,
    "ChoppedVar" integer NOT NULL,
    "ProductAggregation" integer NOT NULL,
    "IndustryAggregation" integer NOT NULL,
    "GrossNet" integer NOT NULL,
    "EXp" double precision,
    "EXf" double precision,
    "EXu" double precision,
    etapf double precision,
    etafu double precision,
    etapu double precision
);


--
-- Name: AggLevel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."AggLevel" (
    "AggLevelID" integer NOT NULL,
    "AggLevel" text,
    "FullName" text,
    "Description" text
);


--
-- Name: AllIEAData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."AllIEAData" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    "LedgerSide" integer NOT NULL,
    "FlowAggregationPoint" integer NOT NULL,
    "Flow" integer NOT NULL,
    "Product" integer NOT NULL,
    "Unit" integer NOT NULL,
    "Edot" double precision
);


--
-- Name: AllMachineData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."AllMachineData" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Method" integer NOT NULL,
    "Machine" integer NOT NULL,
    "EuProduct" integer NOT NULL,
    "Quantity" integer NOT NULL,
    "Year" integer NOT NULL,
    "Value" double precision
);


--
-- Name: AttributeTables; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."AttributeTables" (
    "TableName" text NOT NULL,
    "NameColumn" text,
    "DescriptionColumn" text,
    "Multiselect" boolean,
    "TableDescription" text
);


--
-- Name: BalancedIEAData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."BalancedIEAData" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    "LedgerSide" integer NOT NULL,
    "FlowAggregationPoint" integer NOT NULL,
    "Flow" integer NOT NULL,
    "Product" integer NOT NULL,
    "Unit" integer NOT NULL,
    "Edot" double precision
);


--
-- Name: Cmats; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Cmats" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: CmatsAgg; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."CmatsAgg" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: CompletedAllocationTables; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."CompletedAllocationTables" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "LedgerSide" integer NOT NULL,
    "FlowAggregationPoint" integer NOT NULL,
    "EfProduct" integer NOT NULL,
    "Machine" integer NOT NULL,
    "EuProduct" integer NOT NULL,
    "Destination" integer NOT NULL,
    "Quantity" integer NOT NULL,
    "Year" integer NOT NULL,
    "Value" double precision,
    "CSource" integer NOT NULL
);


--
-- Name: CompletedEfficiencyTables; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."CompletedEfficiencyTables" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Method" integer NOT NULL,
    "Machine" integer NOT NULL,
    "EuProduct" integer NOT NULL,
    "Quantity" integer NOT NULL,
    "Year" integer NOT NULL,
    "Value" double precision,
    "etafuSource" integer NOT NULL
);


--
-- Name: CompletedPhiuTables; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."CompletedPhiuTables" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Method" integer NOT NULL,
    "Machine" integer NOT NULL,
    "EuProduct" integer NOT NULL,
    "Quantity" integer NOT NULL,
    "Year" integer NOT NULL,
    "Value" double precision,
    "PhiSource" integer NOT NULL
);


--
-- Name: Country; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Country" (
    "CountryID" integer NOT NULL,
    "Country" text,
    "FullName" text,
    "Description" text,
    "IsCountry" boolean,
    "IsAggregation" boolean,
    "IsContinent" boolean,
    "IsCanonicalCountry" boolean
);


--
-- Name: Dataset; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Dataset" (
    "DatasetID" integer NOT NULL,
    "Dataset" text,
    "Public" boolean,
    "FullName" text,
    "Description" text
);


--
-- Name: ECCStage; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."ECCStage" (
    "ECCStageID" integer NOT NULL,
    "ECCStage" text,
    "FullName" text,
    "Description" text
);


--
-- Name: EnergyType; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."EnergyType" (
    "EnergyTypeID" integer NOT NULL,
    "EnergyType" text,
    "FullName" text,
    "Description" text
);


--
-- Name: EtafuPhiuvecs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."EtafuPhiuvecs" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Method" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: EtafuYEIOU; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."EtafuYEIOU" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: EtafuYEIOUagg; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."EtafuYEIOUagg" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: Etafuvecs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Etafuvecs" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Method" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: Etai; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Etai" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "IncludesNEU" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: GrossNet; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."GrossNet" (
    "GrossNetID" integer NOT NULL,
    "GrossNet" text,
    "FullName" text,
    "Description" text
);


--
-- Name: HMWPFUData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."HMWPFUData" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Year" integer NOT NULL,
    "Species" integer NOT NULL,
    "Stage" integer NOT NULL,
    "Sector" integer NOT NULL,
    "Unit" integer NOT NULL,
    "Edot" double precision
);


--
-- Name: HMWPFUDataRaw; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."HMWPFUDataRaw" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Year" integer NOT NULL,
    "Species" integer NOT NULL,
    "Stage" integer NOT NULL,
    "Sector" integer NOT NULL,
    "Unit" integer NOT NULL,
    "Edot" double precision
);


--
-- Name: IEAData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."IEAData" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    "LedgerSide" integer NOT NULL,
    "FlowAggregationPoint" integer NOT NULL,
    "Flow" integer NOT NULL,
    "Product" integer NOT NULL,
    "Unit" integer NOT NULL,
    "Edot" double precision
);


--
-- Name: IEAFlowAggregationPoint; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."IEAFlowAggregationPoint" (
    "IEAFlowAggregationPointID" integer NOT NULL,
    "IEAFlowAggregationPoint" text
);


--
-- Name: IEALedgerSide; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."IEALedgerSide" (
    "IEALedgerSideID" integer NOT NULL,
    "IEALedgerSide" text
);


--
-- Name: IncludesNEU; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."IncludesNEU" (
    "IncludesNEUID" integer NOT NULL,
    "IncludesNEU" boolean,
    "FullName" text,
    "Description" text
);


--
-- Name: IncompleteAllocationTables; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."IncompleteAllocationTables" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "LedgerSide" integer NOT NULL,
    "FlowAggregationPoint" integer NOT NULL,
    "EfProduct" integer NOT NULL,
    "Machine" integer NOT NULL,
    "EuProduct" integer NOT NULL,
    "Destination" integer NOT NULL,
    "Quantity" integer NOT NULL,
    "Year" integer NOT NULL,
    "Value" double precision
);


--
-- Name: IndProdType; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."IndProdType" (
    "IndProdTypeID" integer NOT NULL,
    "IndProdType" text
);


--
-- Name: Index; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Index" (
    "IndexID" integer NOT NULL,
    "Index" text,
    "Order" integer,
    "SankeyColumn" integer
);


--
-- Name: MachineData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."MachineData" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Method" integer NOT NULL,
    "Machine" integer NOT NULL,
    "EuProduct" integer NOT NULL,
    "Quantity" integer NOT NULL,
    "Year" integer NOT NULL,
    "Value" double precision
);


--
-- Name: Method; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Method" (
    "MethodID" integer NOT NULL,
    "Method" text,
    "FullName" text,
    "Description" text
);


--
-- Name: PSUT; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUT" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "IncludesNEU" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTFinalIEA; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTFinalIEA" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTIEA; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTIEA" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTIEAMW; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTIEAMW" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTMW; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTMW" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTMWAllYears; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTMWAllYears" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTMWEnergy; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTMWEnergy" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTReAll; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTReAll" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "IncludesNEU" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTReAllChopAllDsAllGrAll; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTReAllChopAllDsAllGrAll" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "IncludesNEU" integer NOT NULL,
    "Year" integer NOT NULL,
    "ChoppedMat" integer NOT NULL,
    "ChoppedVar" integer NOT NULL,
    "ProductAggregation" integer NOT NULL,
    "IndustryAggregation" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTUsefulIEA; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTUsefulIEA" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTUsefulIEAWithDetails; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTUsefulIEAWithDetails" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTWithNEU; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTWithNEU" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PSUTWithoutNEU; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PSUTWithoutNEU" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: Papers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Papers" (
    "PapersID" integer NOT NULL,
    "Authors" text,
    "Year" integer,
    "Title" text,
    "Journal" text,
    "Volume" text,
    "Number" text,
    "Pages" text,
    doi text,
    "URL" text
);


--
-- Name: PhiConstants; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PhiConstants" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Product" integer NOT NULL,
    phi double precision,
    "IsUseful" boolean NOT NULL
);


--
-- Name: PhiSource; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PhiSource" (
    "PhiSourceID" integer NOT NULL,
    "PhiSource" text
);


--
-- Name: Phipfvecs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Phipfvecs" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Method" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: Phiuvecs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Phiuvecs" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Method" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: Phivecs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Phivecs" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: PhivecsMW; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PhivecsMW" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: Quantity; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Quantity" (
    "QuantityID" integer NOT NULL,
    "Quantity" text
);


--
-- Name: RCType; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."RCType" (
    "RCTypeID" integer NOT NULL,
    "RCType" text,
    "FullName" text,
    "Description" text
);


--
-- Name: SchemaTable; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."SchemaTable" (
    "TableName" text NOT NULL,
    "Colname" text NOT NULL,
    "IsPK" boolean,
    "ColDataType" text,
    "FKTable" text,
    "FKColname" text
);


--
-- Name: SectorAggEtaFU; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."SectorAggEtaFU" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "IncludesNEU" integer NOT NULL,
    "Year" integer NOT NULL,
    "ChoppedMat" integer NOT NULL,
    "ChoppedVar" integer NOT NULL,
    "ProductAggregation" integer NOT NULL,
    "IndustryAggregation" integer NOT NULL,
    "GrossNet" integer NOT NULL,
    "Sector" integer NOT NULL,
    "Final" double precision,
    "Useful" double precision,
    etafu double precision
);


--
-- Name: Species; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Species" (
    "SpeciesID" integer NOT NULL,
    "Species" text
);


--
-- Name: SpecifiedIEAData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."SpecifiedIEAData" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    "LedgerSide" integer NOT NULL,
    "FlowAggregationPoint" integer NOT NULL,
    "Flow" integer NOT NULL,
    "Product" integer NOT NULL,
    "Unit" integer NOT NULL,
    "Edot" double precision
);


--
-- Name: Unit; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Unit" (
    "UnitID" integer NOT NULL,
    "Unit" text,
    "FullName" text,
    "Description" text
);


--
-- Name: Version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Version" (
    "VersionID" integer NOT NULL,
    "Version" text,
    "ReleaseDate" text,
    "Public" boolean,
    "ChangeNotes" text
);


--
-- Name: Year; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Year" (
    "YearID" integer NOT NULL,
    "Year" integer
);


--
-- Name: YfuUEIOUfudetails; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."YfuUEIOUfudetails" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: YfuUEIOUfudetailsEnergy; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."YfuUEIOUfudetailsEnergy" (
    "Dataset" integer NOT NULL,
    "ValidFromVersion" integer NOT NULL,
    "ValidToVersion" integer NOT NULL,
    "Country" integer NOT NULL,
    "Method" integer NOT NULL,
    "EnergyType" integer NOT NULL,
    "LastStage" integer NOT NULL,
    "Year" integer NOT NULL,
    matname integer NOT NULL,
    i integer NOT NULL,
    j integer NOT NULL,
    value double precision
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: matname; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.matname (
    "matnameID" integer NOT NULL,
    matname text,
    "FullName" text,
    "Public" boolean,
    "Description" text,
    "RowFormat" text,
    "ColFormat" text
);


--
-- Name: matnameRCType; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."matnameRCType" (
    matname integer NOT NULL,
    rowtype integer NOT NULL,
    coltype integer NOT NULL
);


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Year", "Species", "Stage", "Sector", "Unit");


--
-- Name: AMWPFUData AMWPFUData_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Year", "Species", "Stage", "Sector", "Unit");


--
-- Name: AggEtaPFU AggEtaPFU_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "IncludesNEU", "Year", "ChoppedMat", "ChoppedVar", "ProductAggregation", "IndustryAggregation", "GrossNet");


--
-- Name: AggLevel AggLevel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggLevel"
    ADD CONSTRAINT "AggLevel_pkey" PRIMARY KEY ("AggLevelID");


--
-- Name: AllIEAData AllIEAData_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", "LedgerSide", "FlowAggregationPoint", "Flow", "Product");


--
-- Name: AllMachineData AllMachineData_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "EnergyType", "LastStage", "Method", "Machine", "EuProduct", "Quantity", "Year");


--
-- Name: AttributeTables AttributeTables_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AttributeTables"
    ADD CONSTRAINT "AttributeTables_pkey" PRIMARY KEY ("TableName");


--
-- Name: BalancedIEAData BalancedIEAData_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", "LedgerSide", "FlowAggregationPoint", "Flow", "Product");


--
-- Name: CmatsAgg CmatsAgg_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: Cmats Cmats_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: CompletedAllocationTables CompletedAllocationTables_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "LedgerSide", "FlowAggregationPoint", "EfProduct", "Machine", "EuProduct", "Destination", "Quantity", "Year", "CSource");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "EnergyType", "LastStage", "Method", "Machine", "EuProduct", "Quantity", "Year", "etafuSource");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "EnergyType", "LastStage", "Method", "Machine", "EuProduct", "Quantity", "Year", "PhiSource");


--
-- Name: Country Country_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Country"
    ADD CONSTRAINT "Country_pkey" PRIMARY KEY ("CountryID");


--
-- Name: Dataset Dataset_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Dataset"
    ADD CONSTRAINT "Dataset_pkey" PRIMARY KEY ("DatasetID");


--
-- Name: ECCStage ECCStage_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."ECCStage"
    ADD CONSTRAINT "ECCStage_pkey" PRIMARY KEY ("ECCStageID");


--
-- Name: EnergyType EnergyType_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EnergyType"
    ADD CONSTRAINT "EnergyType_pkey" PRIMARY KEY ("EnergyTypeID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "EnergyType", "LastStage", "Method", "Year", matname, i, j);


--
-- Name: EtafuYEIOU EtafuYEIOU_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "Year", matname, i, j);


--
-- Name: Etafuvecs Etafuvecs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "EnergyType", "LastStage", "Method", "Year", matname, i, j);


--
-- Name: Etai Etai_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "IncludesNEU", "Year", matname, i, j);


--
-- Name: GrossNet GrossNet_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."GrossNet"
    ADD CONSTRAINT "GrossNet_pkey" PRIMARY KEY ("GrossNetID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Year", "Species", "Stage", "Sector", "Unit");


--
-- Name: HMWPFUData HMWPFUData_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Year", "Species", "Stage", "Sector", "Unit");


--
-- Name: IEAData IEAData_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", "LedgerSide", "FlowAggregationPoint", "Flow", "Product");


--
-- Name: IEAFlowAggregationPoint IEAFlowAggregationPoint_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAFlowAggregationPoint"
    ADD CONSTRAINT "IEAFlowAggregationPoint_pkey" PRIMARY KEY ("IEAFlowAggregationPointID");


--
-- Name: IEALedgerSide IEALedgerSide_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEALedgerSide"
    ADD CONSTRAINT "IEALedgerSide_pkey" PRIMARY KEY ("IEALedgerSideID");


--
-- Name: IncludesNEU IncludesNEU_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncludesNEU"
    ADD CONSTRAINT "IncludesNEU_pkey" PRIMARY KEY ("IncludesNEUID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "LedgerSide", "FlowAggregationPoint", "EfProduct", "Machine", "EuProduct", "Destination", "Quantity", "Year");


--
-- Name: IndProdType IndProdType_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IndProdType"
    ADD CONSTRAINT "IndProdType_pkey" PRIMARY KEY ("IndProdTypeID");


--
-- Name: Index Index_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Index"
    ADD CONSTRAINT "Index_pkey" PRIMARY KEY ("IndexID");


--
-- Name: MachineData MachineData_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "EnergyType", "LastStage", "Method", "Machine", "EuProduct", "Quantity", "Year");


--
-- Name: Method Method_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Method"
    ADD CONSTRAINT "Method_pkey" PRIMARY KEY ("MethodID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTIEAMW PSUTIEAMW_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTIEA PSUTIEA_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTMWAllYears PSUTMWAllYears_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTMWEnergy PSUTMWEnergy_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTMW PSUTMW_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "IncludesNEU", "Year", "ChoppedMat", "ChoppedVar", "ProductAggregation", "IndustryAggregation", matname, i, j);


--
-- Name: PSUTReAll PSUTReAll_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "IncludesNEU", "Year", matname, i, j);


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTWithNEU PSUTWithNEU_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: PSUT PSUT_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "IncludesNEU", "Year", matname, i, j);


--
-- Name: Papers Papers_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Papers"
    ADD CONSTRAINT "Papers_pkey" PRIMARY KEY ("PapersID");


--
-- Name: PhiConstants PhiConstants_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhiConstants"
    ADD CONSTRAINT "PhiConstants_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Product", "IsUseful");


--
-- Name: PhiSource PhiSource_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhiSource"
    ADD CONSTRAINT "PhiSource_pkey" PRIMARY KEY ("PhiSourceID");


--
-- Name: Phipfvecs Phipfvecs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "EnergyType", "LastStage", "Method", "Year", matname, i, j);


--
-- Name: Phiuvecs Phiuvecs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "EnergyType", "LastStage", "Method", "Year", matname, i, j);


--
-- Name: PhivecsMW PhivecsMW_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Year", matname, i, j);


--
-- Name: Phivecs Phivecs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Year", matname, i, j);


--
-- Name: Quantity Quantity_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Quantity"
    ADD CONSTRAINT "Quantity_pkey" PRIMARY KEY ("QuantityID");


--
-- Name: RCType RCType_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."RCType"
    ADD CONSTRAINT "RCType_pkey" PRIMARY KEY ("RCTypeID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "IncludesNEU", "Year", "ChoppedMat", "ChoppedVar", "ProductAggregation", "IndustryAggregation", "GrossNet", "Sector");


--
-- Name: Species Species_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Species"
    ADD CONSTRAINT "Species_pkey" PRIMARY KEY ("SpeciesID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", "LedgerSide", "FlowAggregationPoint", "Flow", "Product");


--
-- Name: SchemaTable TableSchema_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SchemaTable"
    ADD CONSTRAINT "TableSchema_pkey" PRIMARY KEY ("TableName", "Colname");


--
-- Name: Unit Unit_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Unit"
    ADD CONSTRAINT "Unit_pkey" PRIMARY KEY ("UnitID");


--
-- Name: Version Version_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Version"
    ADD CONSTRAINT "Version_pkey" PRIMARY KEY ("VersionID");


--
-- Name: Year Year_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Year"
    ADD CONSTRAINT "Year_pkey" PRIMARY KEY ("YearID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_pkey" PRIMARY KEY ("Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "Year", matname, i, j);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: matnameRCType matnameRCType_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."matnameRCType"
    ADD CONSTRAINT "matnameRCType_pkey" PRIMARY KEY (matname);


--
-- Name: matname matname_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matname
    ADD CONSTRAINT matname_pkey PRIMARY KEY ("matnameID");


--
-- Name: aggetapfu__choppedmat; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__choppedmat ON public."AggEtaPFU" USING btree ("ChoppedMat");


--
-- Name: aggetapfu__choppedvar; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__choppedvar ON public."AggEtaPFU" USING btree ("ChoppedVar");


--
-- Name: aggetapfu__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__country ON public."AggEtaPFU" USING btree ("Country");


--
-- Name: aggetapfu__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__dataset ON public."AggEtaPFU" USING btree ("Dataset");


--
-- Name: aggetapfu__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__energytype ON public."AggEtaPFU" USING btree ("EnergyType");


--
-- Name: aggetapfu__grossnet; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__grossnet ON public."AggEtaPFU" USING btree ("GrossNet");


--
-- Name: aggetapfu__includesneu; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__includesneu ON public."AggEtaPFU" USING btree ("IncludesNEU");


--
-- Name: aggetapfu__industryaggregation; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__industryaggregation ON public."AggEtaPFU" USING btree ("IndustryAggregation");


--
-- Name: aggetapfu__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__laststage ON public."AggEtaPFU" USING btree ("LastStage");


--
-- Name: aggetapfu__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__method ON public."AggEtaPFU" USING btree ("Method");


--
-- Name: aggetapfu__productaggregation; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__productaggregation ON public."AggEtaPFU" USING btree ("ProductAggregation");


--
-- Name: aggetapfu__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__validfromversion ON public."AggEtaPFU" USING btree ("ValidFromVersion");


--
-- Name: aggetapfu__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__validtoversion ON public."AggEtaPFU" USING btree ("ValidToVersion");


--
-- Name: aggetapfu__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX aggetapfu__year ON public."AggEtaPFU" USING btree ("Year");


--
-- Name: allieadata__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__country ON public."AllIEAData" USING btree ("Country");


--
-- Name: allieadata__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__dataset ON public."AllIEAData" USING btree ("Dataset");


--
-- Name: allieadata__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__energytype ON public."AllIEAData" USING btree ("EnergyType");


--
-- Name: allieadata__flow; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__flow ON public."AllIEAData" USING btree ("Flow");


--
-- Name: allieadata__flowaggregationpoint; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__flowaggregationpoint ON public."AllIEAData" USING btree ("FlowAggregationPoint");


--
-- Name: allieadata__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__laststage ON public."AllIEAData" USING btree ("LastStage");


--
-- Name: allieadata__ledgerside; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__ledgerside ON public."AllIEAData" USING btree ("LedgerSide");


--
-- Name: allieadata__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__method ON public."AllIEAData" USING btree ("Method");


--
-- Name: allieadata__product; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__product ON public."AllIEAData" USING btree ("Product");


--
-- Name: allieadata__unit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__unit ON public."AllIEAData" USING btree ("Unit");


--
-- Name: allieadata__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__validfromversion ON public."AllIEAData" USING btree ("ValidFromVersion");


--
-- Name: allieadata__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__validtoversion ON public."AllIEAData" USING btree ("ValidToVersion");


--
-- Name: allieadata__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allieadata__year ON public."AllIEAData" USING btree ("Year");


--
-- Name: allmachinedata__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__country ON public."AllMachineData" USING btree ("Country");


--
-- Name: allmachinedata__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__dataset ON public."AllMachineData" USING btree ("Dataset");


--
-- Name: allmachinedata__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__energytype ON public."AllMachineData" USING btree ("EnergyType");


--
-- Name: allmachinedata__euproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__euproduct ON public."AllMachineData" USING btree ("EuProduct");


--
-- Name: allmachinedata__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__laststage ON public."AllMachineData" USING btree ("LastStage");


--
-- Name: allmachinedata__machine; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__machine ON public."AllMachineData" USING btree ("Machine");


--
-- Name: allmachinedata__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__method ON public."AllMachineData" USING btree ("Method");


--
-- Name: allmachinedata__quantity; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__quantity ON public."AllMachineData" USING btree ("Quantity");


--
-- Name: allmachinedata__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__validfromversion ON public."AllMachineData" USING btree ("ValidFromVersion");


--
-- Name: allmachinedata__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__validtoversion ON public."AllMachineData" USING btree ("ValidToVersion");


--
-- Name: allmachinedata__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX allmachinedata__year ON public."AllMachineData" USING btree ("Year");


--
-- Name: amwpfudata__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__country ON public."AMWPFUData" USING btree ("Country");


--
-- Name: amwpfudata__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__dataset ON public."AMWPFUData" USING btree ("Dataset");


--
-- Name: amwpfudata__sector; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__sector ON public."AMWPFUData" USING btree ("Sector");


--
-- Name: amwpfudata__species; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__species ON public."AMWPFUData" USING btree ("Species");


--
-- Name: amwpfudata__stage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__stage ON public."AMWPFUData" USING btree ("Stage");


--
-- Name: amwpfudata__unit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__unit ON public."AMWPFUData" USING btree ("Unit");


--
-- Name: amwpfudata__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__validfromversion ON public."AMWPFUData" USING btree ("ValidFromVersion");


--
-- Name: amwpfudata__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__validtoversion ON public."AMWPFUData" USING btree ("ValidToVersion");


--
-- Name: amwpfudata__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudata__year ON public."AMWPFUData" USING btree ("Year");


--
-- Name: amwpfudataraw__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__country ON public."AMWPFUDataRaw" USING btree ("Country");


--
-- Name: amwpfudataraw__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__dataset ON public."AMWPFUDataRaw" USING btree ("Dataset");


--
-- Name: amwpfudataraw__sector; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__sector ON public."AMWPFUDataRaw" USING btree ("Sector");


--
-- Name: amwpfudataraw__species; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__species ON public."AMWPFUDataRaw" USING btree ("Species");


--
-- Name: amwpfudataraw__stage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__stage ON public."AMWPFUDataRaw" USING btree ("Stage");


--
-- Name: amwpfudataraw__unit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__unit ON public."AMWPFUDataRaw" USING btree ("Unit");


--
-- Name: amwpfudataraw__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__validfromversion ON public."AMWPFUDataRaw" USING btree ("ValidFromVersion");


--
-- Name: amwpfudataraw__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__validtoversion ON public."AMWPFUDataRaw" USING btree ("ValidToVersion");


--
-- Name: amwpfudataraw__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX amwpfudataraw__year ON public."AMWPFUDataRaw" USING btree ("Year");


--
-- Name: balancedieadata__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__country ON public."BalancedIEAData" USING btree ("Country");


--
-- Name: balancedieadata__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__dataset ON public."BalancedIEAData" USING btree ("Dataset");


--
-- Name: balancedieadata__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__energytype ON public."BalancedIEAData" USING btree ("EnergyType");


--
-- Name: balancedieadata__flow; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__flow ON public."BalancedIEAData" USING btree ("Flow");


--
-- Name: balancedieadata__flowaggregationpoint; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__flowaggregationpoint ON public."BalancedIEAData" USING btree ("FlowAggregationPoint");


--
-- Name: balancedieadata__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__laststage ON public."BalancedIEAData" USING btree ("LastStage");


--
-- Name: balancedieadata__ledgerside; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__ledgerside ON public."BalancedIEAData" USING btree ("LedgerSide");


--
-- Name: balancedieadata__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__method ON public."BalancedIEAData" USING btree ("Method");


--
-- Name: balancedieadata__product; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__product ON public."BalancedIEAData" USING btree ("Product");


--
-- Name: balancedieadata__unit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__unit ON public."BalancedIEAData" USING btree ("Unit");


--
-- Name: balancedieadata__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__validfromversion ON public."BalancedIEAData" USING btree ("ValidFromVersion");


--
-- Name: balancedieadata__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__validtoversion ON public."BalancedIEAData" USING btree ("ValidToVersion");


--
-- Name: balancedieadata__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX balancedieadata__year ON public."BalancedIEAData" USING btree ("Year");


--
-- Name: cmats__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__country ON public."Cmats" USING btree ("Country");


--
-- Name: cmats__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__dataset ON public."Cmats" USING btree ("Dataset");


--
-- Name: cmats__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__energytype ON public."Cmats" USING btree ("EnergyType");


--
-- Name: cmats__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__i ON public."Cmats" USING btree (i);


--
-- Name: cmats__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__j ON public."Cmats" USING btree (j);


--
-- Name: cmats__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__laststage ON public."Cmats" USING btree ("LastStage");


--
-- Name: cmats__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__matname ON public."Cmats" USING btree (matname);


--
-- Name: cmats__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__method ON public."Cmats" USING btree ("Method");


--
-- Name: cmats__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__validfromversion ON public."Cmats" USING btree ("ValidFromVersion");


--
-- Name: cmats__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__validtoversion ON public."Cmats" USING btree ("ValidToVersion");


--
-- Name: cmats__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmats__year ON public."Cmats" USING btree ("Year");


--
-- Name: cmatsagg__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__country ON public."CmatsAgg" USING btree ("Country");


--
-- Name: cmatsagg__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__dataset ON public."CmatsAgg" USING btree ("Dataset");


--
-- Name: cmatsagg__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__energytype ON public."CmatsAgg" USING btree ("EnergyType");


--
-- Name: cmatsagg__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__i ON public."CmatsAgg" USING btree (i);


--
-- Name: cmatsagg__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__j ON public."CmatsAgg" USING btree (j);


--
-- Name: cmatsagg__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__laststage ON public."CmatsAgg" USING btree ("LastStage");


--
-- Name: cmatsagg__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__matname ON public."CmatsAgg" USING btree (matname);


--
-- Name: cmatsagg__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__method ON public."CmatsAgg" USING btree ("Method");


--
-- Name: cmatsagg__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__validfromversion ON public."CmatsAgg" USING btree ("ValidFromVersion");


--
-- Name: cmatsagg__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__validtoversion ON public."CmatsAgg" USING btree ("ValidToVersion");


--
-- Name: cmatsagg__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cmatsagg__year ON public."CmatsAgg" USING btree ("Year");


--
-- Name: completedallocationtables__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__country ON public."CompletedAllocationTables" USING btree ("Country");


--
-- Name: completedallocationtables__csource; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__csource ON public."CompletedAllocationTables" USING btree ("CSource");


--
-- Name: completedallocationtables__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__dataset ON public."CompletedAllocationTables" USING btree ("Dataset");


--
-- Name: completedallocationtables__destination; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__destination ON public."CompletedAllocationTables" USING btree ("Destination");


--
-- Name: completedallocationtables__efproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__efproduct ON public."CompletedAllocationTables" USING btree ("EfProduct");


--
-- Name: completedallocationtables__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__energytype ON public."CompletedAllocationTables" USING btree ("EnergyType");


--
-- Name: completedallocationtables__euproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__euproduct ON public."CompletedAllocationTables" USING btree ("EuProduct");


--
-- Name: completedallocationtables__flowaggregationpoint; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__flowaggregationpoint ON public."CompletedAllocationTables" USING btree ("FlowAggregationPoint");


--
-- Name: completedallocationtables__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__laststage ON public."CompletedAllocationTables" USING btree ("LastStage");


--
-- Name: completedallocationtables__ledgerside; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__ledgerside ON public."CompletedAllocationTables" USING btree ("LedgerSide");


--
-- Name: completedallocationtables__machine; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__machine ON public."CompletedAllocationTables" USING btree ("Machine");


--
-- Name: completedallocationtables__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__method ON public."CompletedAllocationTables" USING btree ("Method");


--
-- Name: completedallocationtables__quantity; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__quantity ON public."CompletedAllocationTables" USING btree ("Quantity");


--
-- Name: completedallocationtables__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__validfromversion ON public."CompletedAllocationTables" USING btree ("ValidFromVersion");


--
-- Name: completedallocationtables__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__validtoversion ON public."CompletedAllocationTables" USING btree ("ValidToVersion");


--
-- Name: completedallocationtables__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedallocationtables__year ON public."CompletedAllocationTables" USING btree ("Year");


--
-- Name: completedefficiencytables__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__country ON public."CompletedEfficiencyTables" USING btree ("Country");


--
-- Name: completedefficiencytables__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__dataset ON public."CompletedEfficiencyTables" USING btree ("Dataset");


--
-- Name: completedefficiencytables__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__energytype ON public."CompletedEfficiencyTables" USING btree ("EnergyType");


--
-- Name: completedefficiencytables__etafusource; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__etafusource ON public."CompletedEfficiencyTables" USING btree ("etafuSource");


--
-- Name: completedefficiencytables__euproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__euproduct ON public."CompletedEfficiencyTables" USING btree ("EuProduct");


--
-- Name: completedefficiencytables__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__laststage ON public."CompletedEfficiencyTables" USING btree ("LastStage");


--
-- Name: completedefficiencytables__machine; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__machine ON public."CompletedEfficiencyTables" USING btree ("Machine");


--
-- Name: completedefficiencytables__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__method ON public."CompletedEfficiencyTables" USING btree ("Method");


--
-- Name: completedefficiencytables__quantity; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__quantity ON public."CompletedEfficiencyTables" USING btree ("Quantity");


--
-- Name: completedefficiencytables__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__validfromversion ON public."CompletedEfficiencyTables" USING btree ("ValidFromVersion");


--
-- Name: completedefficiencytables__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__validtoversion ON public."CompletedEfficiencyTables" USING btree ("ValidToVersion");


--
-- Name: completedefficiencytables__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedefficiencytables__year ON public."CompletedEfficiencyTables" USING btree ("Year");


--
-- Name: completedphiutables__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__country ON public."CompletedPhiuTables" USING btree ("Country");


--
-- Name: completedphiutables__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__dataset ON public."CompletedPhiuTables" USING btree ("Dataset");


--
-- Name: completedphiutables__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__energytype ON public."CompletedPhiuTables" USING btree ("EnergyType");


--
-- Name: completedphiutables__euproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__euproduct ON public."CompletedPhiuTables" USING btree ("EuProduct");


--
-- Name: completedphiutables__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__laststage ON public."CompletedPhiuTables" USING btree ("LastStage");


--
-- Name: completedphiutables__machine; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__machine ON public."CompletedPhiuTables" USING btree ("Machine");


--
-- Name: completedphiutables__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__method ON public."CompletedPhiuTables" USING btree ("Method");


--
-- Name: completedphiutables__phisource; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__phisource ON public."CompletedPhiuTables" USING btree ("PhiSource");


--
-- Name: completedphiutables__quantity; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__quantity ON public."CompletedPhiuTables" USING btree ("Quantity");


--
-- Name: completedphiutables__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__validfromversion ON public."CompletedPhiuTables" USING btree ("ValidFromVersion");


--
-- Name: completedphiutables__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__validtoversion ON public."CompletedPhiuTables" USING btree ("ValidToVersion");


--
-- Name: completedphiutables__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX completedphiutables__year ON public."CompletedPhiuTables" USING btree ("Year");


--
-- Name: etafuphiuvecs__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__country ON public."EtafuPhiuvecs" USING btree ("Country");


--
-- Name: etafuphiuvecs__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__dataset ON public."EtafuPhiuvecs" USING btree ("Dataset");


--
-- Name: etafuphiuvecs__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__energytype ON public."EtafuPhiuvecs" USING btree ("EnergyType");


--
-- Name: etafuphiuvecs__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__i ON public."EtafuPhiuvecs" USING btree (i);


--
-- Name: etafuphiuvecs__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__j ON public."EtafuPhiuvecs" USING btree (j);


--
-- Name: etafuphiuvecs__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__laststage ON public."EtafuPhiuvecs" USING btree ("LastStage");


--
-- Name: etafuphiuvecs__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__matname ON public."EtafuPhiuvecs" USING btree (matname);


--
-- Name: etafuphiuvecs__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__method ON public."EtafuPhiuvecs" USING btree ("Method");


--
-- Name: etafuphiuvecs__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__validfromversion ON public."EtafuPhiuvecs" USING btree ("ValidFromVersion");


--
-- Name: etafuphiuvecs__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__validtoversion ON public."EtafuPhiuvecs" USING btree ("ValidToVersion");


--
-- Name: etafuphiuvecs__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuphiuvecs__year ON public."EtafuPhiuvecs" USING btree ("Year");


--
-- Name: etafuvecs__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__country ON public."Etafuvecs" USING btree ("Country");


--
-- Name: etafuvecs__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__dataset ON public."Etafuvecs" USING btree ("Dataset");


--
-- Name: etafuvecs__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__energytype ON public."Etafuvecs" USING btree ("EnergyType");


--
-- Name: etafuvecs__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__i ON public."Etafuvecs" USING btree (i);


--
-- Name: etafuvecs__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__j ON public."Etafuvecs" USING btree (j);


--
-- Name: etafuvecs__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__laststage ON public."Etafuvecs" USING btree ("LastStage");


--
-- Name: etafuvecs__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__matname ON public."Etafuvecs" USING btree (matname);


--
-- Name: etafuvecs__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__method ON public."Etafuvecs" USING btree ("Method");


--
-- Name: etafuvecs__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__validfromversion ON public."Etafuvecs" USING btree ("ValidFromVersion");


--
-- Name: etafuvecs__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__validtoversion ON public."Etafuvecs" USING btree ("ValidToVersion");


--
-- Name: etafuvecs__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuvecs__year ON public."Etafuvecs" USING btree ("Year");


--
-- Name: etafuyeiou__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__country ON public."EtafuYEIOU" USING btree ("Country");


--
-- Name: etafuyeiou__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__dataset ON public."EtafuYEIOU" USING btree ("Dataset");


--
-- Name: etafuyeiou__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__energytype ON public."EtafuYEIOU" USING btree ("EnergyType");


--
-- Name: etafuyeiou__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__i ON public."EtafuYEIOU" USING btree (i);


--
-- Name: etafuyeiou__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__j ON public."EtafuYEIOU" USING btree (j);


--
-- Name: etafuyeiou__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__laststage ON public."EtafuYEIOU" USING btree ("LastStage");


--
-- Name: etafuyeiou__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__matname ON public."EtafuYEIOU" USING btree (matname);


--
-- Name: etafuyeiou__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__method ON public."EtafuYEIOU" USING btree ("Method");


--
-- Name: etafuyeiou__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__validfromversion ON public."EtafuYEIOU" USING btree ("ValidFromVersion");


--
-- Name: etafuyeiou__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__validtoversion ON public."EtafuYEIOU" USING btree ("ValidToVersion");


--
-- Name: etafuyeiou__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiou__year ON public."EtafuYEIOU" USING btree ("Year");


--
-- Name: etafuyeiouagg__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__country ON public."EtafuYEIOUagg" USING btree ("Country");


--
-- Name: etafuyeiouagg__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__dataset ON public."EtafuYEIOUagg" USING btree ("Dataset");


--
-- Name: etafuyeiouagg__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__energytype ON public."EtafuYEIOUagg" USING btree ("EnergyType");


--
-- Name: etafuyeiouagg__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__i ON public."EtafuYEIOUagg" USING btree (i);


--
-- Name: etafuyeiouagg__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__j ON public."EtafuYEIOUagg" USING btree (j);


--
-- Name: etafuyeiouagg__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__matname ON public."EtafuYEIOUagg" USING btree (matname);


--
-- Name: etafuyeiouagg__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__method ON public."EtafuYEIOUagg" USING btree ("Method");


--
-- Name: etafuyeiouagg__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__validfromversion ON public."EtafuYEIOUagg" USING btree ("ValidFromVersion");


--
-- Name: etafuyeiouagg__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__validtoversion ON public."EtafuYEIOUagg" USING btree ("ValidToVersion");


--
-- Name: etafuyeiouagg__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etafuyeiouagg__year ON public."EtafuYEIOUagg" USING btree ("Year");


--
-- Name: etai__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__country ON public."Etai" USING btree ("Country");


--
-- Name: etai__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__dataset ON public."Etai" USING btree ("Dataset");


--
-- Name: etai__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__energytype ON public."Etai" USING btree ("EnergyType");


--
-- Name: etai__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__i ON public."Etai" USING btree (i);


--
-- Name: etai__includesneu; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__includesneu ON public."Etai" USING btree ("IncludesNEU");


--
-- Name: etai__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__j ON public."Etai" USING btree (j);


--
-- Name: etai__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__laststage ON public."Etai" USING btree ("LastStage");


--
-- Name: etai__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__matname ON public."Etai" USING btree (matname);


--
-- Name: etai__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__method ON public."Etai" USING btree ("Method");


--
-- Name: etai__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__validfromversion ON public."Etai" USING btree ("ValidFromVersion");


--
-- Name: etai__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__validtoversion ON public."Etai" USING btree ("ValidToVersion");


--
-- Name: etai__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX etai__year ON public."Etai" USING btree ("Year");


--
-- Name: hmwpfudata__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__country ON public."HMWPFUData" USING btree ("Country");


--
-- Name: hmwpfudata__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__dataset ON public."HMWPFUData" USING btree ("Dataset");


--
-- Name: hmwpfudata__sector; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__sector ON public."HMWPFUData" USING btree ("Sector");


--
-- Name: hmwpfudata__species; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__species ON public."HMWPFUData" USING btree ("Species");


--
-- Name: hmwpfudata__stage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__stage ON public."HMWPFUData" USING btree ("Stage");


--
-- Name: hmwpfudata__unit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__unit ON public."HMWPFUData" USING btree ("Unit");


--
-- Name: hmwpfudata__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__validfromversion ON public."HMWPFUData" USING btree ("ValidFromVersion");


--
-- Name: hmwpfudata__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__validtoversion ON public."HMWPFUData" USING btree ("ValidToVersion");


--
-- Name: hmwpfudata__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudata__year ON public."HMWPFUData" USING btree ("Year");


--
-- Name: hmwpfudataraw__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__country ON public."HMWPFUDataRaw" USING btree ("Country");


--
-- Name: hmwpfudataraw__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__dataset ON public."HMWPFUDataRaw" USING btree ("Dataset");


--
-- Name: hmwpfudataraw__sector; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__sector ON public."HMWPFUDataRaw" USING btree ("Sector");


--
-- Name: hmwpfudataraw__species; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__species ON public."HMWPFUDataRaw" USING btree ("Species");


--
-- Name: hmwpfudataraw__stage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__stage ON public."HMWPFUDataRaw" USING btree ("Stage");


--
-- Name: hmwpfudataraw__unit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__unit ON public."HMWPFUDataRaw" USING btree ("Unit");


--
-- Name: hmwpfudataraw__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__validfromversion ON public."HMWPFUDataRaw" USING btree ("ValidFromVersion");


--
-- Name: hmwpfudataraw__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__validtoversion ON public."HMWPFUDataRaw" USING btree ("ValidToVersion");


--
-- Name: hmwpfudataraw__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hmwpfudataraw__year ON public."HMWPFUDataRaw" USING btree ("Year");


--
-- Name: ieadata__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__country ON public."IEAData" USING btree ("Country");


--
-- Name: ieadata__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__dataset ON public."IEAData" USING btree ("Dataset");


--
-- Name: ieadata__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__energytype ON public."IEAData" USING btree ("EnergyType");


--
-- Name: ieadata__flow; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__flow ON public."IEAData" USING btree ("Flow");


--
-- Name: ieadata__flowaggregationpoint; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__flowaggregationpoint ON public."IEAData" USING btree ("FlowAggregationPoint");


--
-- Name: ieadata__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__laststage ON public."IEAData" USING btree ("LastStage");


--
-- Name: ieadata__ledgerside; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__ledgerside ON public."IEAData" USING btree ("LedgerSide");


--
-- Name: ieadata__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__method ON public."IEAData" USING btree ("Method");


--
-- Name: ieadata__product; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__product ON public."IEAData" USING btree ("Product");


--
-- Name: ieadata__unit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__unit ON public."IEAData" USING btree ("Unit");


--
-- Name: ieadata__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__validfromversion ON public."IEAData" USING btree ("ValidFromVersion");


--
-- Name: ieadata__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__validtoversion ON public."IEAData" USING btree ("ValidToVersion");


--
-- Name: ieadata__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ieadata__year ON public."IEAData" USING btree ("Year");


--
-- Name: incompleteallocationtables__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__country ON public."IncompleteAllocationTables" USING btree ("Country");


--
-- Name: incompleteallocationtables__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__dataset ON public."IncompleteAllocationTables" USING btree ("Dataset");


--
-- Name: incompleteallocationtables__destination; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__destination ON public."IncompleteAllocationTables" USING btree ("Destination");


--
-- Name: incompleteallocationtables__efproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__efproduct ON public."IncompleteAllocationTables" USING btree ("EfProduct");


--
-- Name: incompleteallocationtables__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__energytype ON public."IncompleteAllocationTables" USING btree ("EnergyType");


--
-- Name: incompleteallocationtables__euproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__euproduct ON public."IncompleteAllocationTables" USING btree ("EuProduct");


--
-- Name: incompleteallocationtables__flowaggregationpoint; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__flowaggregationpoint ON public."IncompleteAllocationTables" USING btree ("FlowAggregationPoint");


--
-- Name: incompleteallocationtables__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__laststage ON public."IncompleteAllocationTables" USING btree ("LastStage");


--
-- Name: incompleteallocationtables__ledgerside; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__ledgerside ON public."IncompleteAllocationTables" USING btree ("LedgerSide");


--
-- Name: incompleteallocationtables__machine; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__machine ON public."IncompleteAllocationTables" USING btree ("Machine");


--
-- Name: incompleteallocationtables__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__method ON public."IncompleteAllocationTables" USING btree ("Method");


--
-- Name: incompleteallocationtables__quantity; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__quantity ON public."IncompleteAllocationTables" USING btree ("Quantity");


--
-- Name: incompleteallocationtables__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__validfromversion ON public."IncompleteAllocationTables" USING btree ("ValidFromVersion");


--
-- Name: incompleteallocationtables__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__validtoversion ON public."IncompleteAllocationTables" USING btree ("ValidToVersion");


--
-- Name: incompleteallocationtables__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX incompleteallocationtables__year ON public."IncompleteAllocationTables" USING btree ("Year");


--
-- Name: machinedata__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__country ON public."MachineData" USING btree ("Country");


--
-- Name: machinedata__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__dataset ON public."MachineData" USING btree ("Dataset");


--
-- Name: machinedata__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__energytype ON public."MachineData" USING btree ("EnergyType");


--
-- Name: machinedata__euproduct; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__euproduct ON public."MachineData" USING btree ("EuProduct");


--
-- Name: machinedata__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__laststage ON public."MachineData" USING btree ("LastStage");


--
-- Name: machinedata__machine; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__machine ON public."MachineData" USING btree ("Machine");


--
-- Name: machinedata__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__method ON public."MachineData" USING btree ("Method");


--
-- Name: machinedata__quantity; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__quantity ON public."MachineData" USING btree ("Quantity");


--
-- Name: machinedata__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__validfromversion ON public."MachineData" USING btree ("ValidFromVersion");


--
-- Name: machinedata__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__validtoversion ON public."MachineData" USING btree ("ValidToVersion");


--
-- Name: machinedata__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX machinedata__year ON public."MachineData" USING btree ("Year");


--
-- Name: matnamerctype__coltype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX matnamerctype__coltype ON public."matnameRCType" USING btree (coltype);


--
-- Name: matnamerctype__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX matnamerctype__matname ON public."matnameRCType" USING btree (matname);


--
-- Name: matnamerctype__rowtype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX matnamerctype__rowtype ON public."matnameRCType" USING btree (rowtype);


--
-- Name: phiconstants__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiconstants__dataset ON public."PhiConstants" USING btree ("Dataset");


--
-- Name: phiconstants__product; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiconstants__product ON public."PhiConstants" USING btree ("Product");


--
-- Name: phiconstants__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiconstants__validfromversion ON public."PhiConstants" USING btree ("ValidFromVersion");


--
-- Name: phiconstants__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiconstants__validtoversion ON public."PhiConstants" USING btree ("ValidToVersion");


--
-- Name: phipfvecs__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__country ON public."Phipfvecs" USING btree ("Country");


--
-- Name: phipfvecs__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__dataset ON public."Phipfvecs" USING btree ("Dataset");


--
-- Name: phipfvecs__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__energytype ON public."Phipfvecs" USING btree ("EnergyType");


--
-- Name: phipfvecs__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__i ON public."Phipfvecs" USING btree (i);


--
-- Name: phipfvecs__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__j ON public."Phipfvecs" USING btree (j);


--
-- Name: phipfvecs__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__laststage ON public."Phipfvecs" USING btree ("LastStage");


--
-- Name: phipfvecs__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__matname ON public."Phipfvecs" USING btree (matname);


--
-- Name: phipfvecs__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__method ON public."Phipfvecs" USING btree ("Method");


--
-- Name: phipfvecs__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__validfromversion ON public."Phipfvecs" USING btree ("ValidFromVersion");


--
-- Name: phipfvecs__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__validtoversion ON public."Phipfvecs" USING btree ("ValidToVersion");


--
-- Name: phipfvecs__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phipfvecs__year ON public."Phipfvecs" USING btree ("Year");


--
-- Name: phiuvecs__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__country ON public."Phiuvecs" USING btree ("Country");


--
-- Name: phiuvecs__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__dataset ON public."Phiuvecs" USING btree ("Dataset");


--
-- Name: phiuvecs__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__energytype ON public."Phiuvecs" USING btree ("EnergyType");


--
-- Name: phiuvecs__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__i ON public."Phiuvecs" USING btree (i);


--
-- Name: phiuvecs__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__j ON public."Phiuvecs" USING btree (j);


--
-- Name: phiuvecs__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__laststage ON public."Phiuvecs" USING btree ("LastStage");


--
-- Name: phiuvecs__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__matname ON public."Phiuvecs" USING btree (matname);


--
-- Name: phiuvecs__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__method ON public."Phiuvecs" USING btree ("Method");


--
-- Name: phiuvecs__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__validfromversion ON public."Phiuvecs" USING btree ("ValidFromVersion");


--
-- Name: phiuvecs__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__validtoversion ON public."Phiuvecs" USING btree ("ValidToVersion");


--
-- Name: phiuvecs__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phiuvecs__year ON public."Phiuvecs" USING btree ("Year");


--
-- Name: phivecs__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecs__country ON public."Phivecs" USING btree ("Country");


--
-- Name: phivecs__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecs__dataset ON public."Phivecs" USING btree ("Dataset");


--
-- Name: phivecs__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecs__i ON public."Phivecs" USING btree (i);


--
-- Name: phivecs__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecs__j ON public."Phivecs" USING btree (j);


--
-- Name: phivecs__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecs__matname ON public."Phivecs" USING btree (matname);


--
-- Name: phivecs__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecs__validfromversion ON public."Phivecs" USING btree ("ValidFromVersion");


--
-- Name: phivecs__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecs__validtoversion ON public."Phivecs" USING btree ("ValidToVersion");


--
-- Name: phivecs__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecs__year ON public."Phivecs" USING btree ("Year");


--
-- Name: phivecsmw__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecsmw__country ON public."PhivecsMW" USING btree ("Country");


--
-- Name: phivecsmw__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecsmw__dataset ON public."PhivecsMW" USING btree ("Dataset");


--
-- Name: phivecsmw__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecsmw__i ON public."PhivecsMW" USING btree (i);


--
-- Name: phivecsmw__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecsmw__j ON public."PhivecsMW" USING btree (j);


--
-- Name: phivecsmw__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecsmw__matname ON public."PhivecsMW" USING btree (matname);


--
-- Name: phivecsmw__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecsmw__validfromversion ON public."PhivecsMW" USING btree ("ValidFromVersion");


--
-- Name: phivecsmw__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecsmw__validtoversion ON public."PhivecsMW" USING btree ("ValidToVersion");


--
-- Name: phivecsmw__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX phivecsmw__year ON public."PhivecsMW" USING btree ("Year");


--
-- Name: psut__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__country ON public."PSUT" USING btree ("Country");


--
-- Name: psut__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__dataset ON public."PSUT" USING btree ("Dataset");


--
-- Name: psut__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__energytype ON public."PSUT" USING btree ("EnergyType");


--
-- Name: psut__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__i ON public."PSUT" USING btree (i);


--
-- Name: psut__includesneu; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__includesneu ON public."PSUT" USING btree ("IncludesNEU");


--
-- Name: psut__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__j ON public."PSUT" USING btree (j);


--
-- Name: psut__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__laststage ON public."PSUT" USING btree ("LastStage");


--
-- Name: psut__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__matname ON public."PSUT" USING btree (matname);


--
-- Name: psut__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__method ON public."PSUT" USING btree ("Method");


--
-- Name: psut__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__validfromversion ON public."PSUT" USING btree ("ValidFromVersion");


--
-- Name: psut__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__validtoversion ON public."PSUT" USING btree ("ValidToVersion");


--
-- Name: psut__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psut__year ON public."PSUT" USING btree ("Year");


--
-- Name: psutfinaliea__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__country ON public."PSUTFinalIEA" USING btree ("Country");


--
-- Name: psutfinaliea__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__dataset ON public."PSUTFinalIEA" USING btree ("Dataset");


--
-- Name: psutfinaliea__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__energytype ON public."PSUTFinalIEA" USING btree ("EnergyType");


--
-- Name: psutfinaliea__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__i ON public."PSUTFinalIEA" USING btree (i);


--
-- Name: psutfinaliea__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__j ON public."PSUTFinalIEA" USING btree (j);


--
-- Name: psutfinaliea__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__laststage ON public."PSUTFinalIEA" USING btree ("LastStage");


--
-- Name: psutfinaliea__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__matname ON public."PSUTFinalIEA" USING btree (matname);


--
-- Name: psutfinaliea__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__method ON public."PSUTFinalIEA" USING btree ("Method");


--
-- Name: psutfinaliea__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__validfromversion ON public."PSUTFinalIEA" USING btree ("ValidFromVersion");


--
-- Name: psutfinaliea__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__validtoversion ON public."PSUTFinalIEA" USING btree ("ValidToVersion");


--
-- Name: psutfinaliea__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutfinaliea__year ON public."PSUTFinalIEA" USING btree ("Year");


--
-- Name: psutiea__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__country ON public."PSUTIEA" USING btree ("Country");


--
-- Name: psutiea__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__dataset ON public."PSUTIEA" USING btree ("Dataset");


--
-- Name: psutiea__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__energytype ON public."PSUTIEA" USING btree ("EnergyType");


--
-- Name: psutiea__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__i ON public."PSUTIEA" USING btree (i);


--
-- Name: psutiea__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__j ON public."PSUTIEA" USING btree (j);


--
-- Name: psutiea__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__laststage ON public."PSUTIEA" USING btree ("LastStage");


--
-- Name: psutiea__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__matname ON public."PSUTIEA" USING btree (matname);


--
-- Name: psutiea__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__method ON public."PSUTIEA" USING btree ("Method");


--
-- Name: psutiea__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__validfromversion ON public."PSUTIEA" USING btree ("ValidFromVersion");


--
-- Name: psutiea__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__validtoversion ON public."PSUTIEA" USING btree ("ValidToVersion");


--
-- Name: psutiea__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutiea__year ON public."PSUTIEA" USING btree ("Year");


--
-- Name: psutieamw__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__country ON public."PSUTIEAMW" USING btree ("Country");


--
-- Name: psutieamw__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__dataset ON public."PSUTIEAMW" USING btree ("Dataset");


--
-- Name: psutieamw__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__energytype ON public."PSUTIEAMW" USING btree ("EnergyType");


--
-- Name: psutieamw__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__i ON public."PSUTIEAMW" USING btree (i);


--
-- Name: psutieamw__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__j ON public."PSUTIEAMW" USING btree (j);


--
-- Name: psutieamw__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__laststage ON public."PSUTIEAMW" USING btree ("LastStage");


--
-- Name: psutieamw__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__matname ON public."PSUTIEAMW" USING btree (matname);


--
-- Name: psutieamw__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__method ON public."PSUTIEAMW" USING btree ("Method");


--
-- Name: psutieamw__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__validfromversion ON public."PSUTIEAMW" USING btree ("ValidFromVersion");


--
-- Name: psutieamw__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__validtoversion ON public."PSUTIEAMW" USING btree ("ValidToVersion");


--
-- Name: psutieamw__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutieamw__year ON public."PSUTIEAMW" USING btree ("Year");


--
-- Name: psutmw__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__country ON public."PSUTMW" USING btree ("Country");


--
-- Name: psutmw__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__dataset ON public."PSUTMW" USING btree ("Dataset");


--
-- Name: psutmw__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__energytype ON public."PSUTMW" USING btree ("EnergyType");


--
-- Name: psutmw__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__i ON public."PSUTMW" USING btree (i);


--
-- Name: psutmw__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__j ON public."PSUTMW" USING btree (j);


--
-- Name: psutmw__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__laststage ON public."PSUTMW" USING btree ("LastStage");


--
-- Name: psutmw__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__matname ON public."PSUTMW" USING btree (matname);


--
-- Name: psutmw__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__method ON public."PSUTMW" USING btree ("Method");


--
-- Name: psutmw__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__validfromversion ON public."PSUTMW" USING btree ("ValidFromVersion");


--
-- Name: psutmw__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__validtoversion ON public."PSUTMW" USING btree ("ValidToVersion");


--
-- Name: psutmw__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmw__year ON public."PSUTMW" USING btree ("Year");


--
-- Name: psutmwallyears__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__country ON public."PSUTMWAllYears" USING btree ("Country");


--
-- Name: psutmwallyears__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__dataset ON public."PSUTMWAllYears" USING btree ("Dataset");


--
-- Name: psutmwallyears__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__energytype ON public."PSUTMWAllYears" USING btree ("EnergyType");


--
-- Name: psutmwallyears__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__i ON public."PSUTMWAllYears" USING btree (i);


--
-- Name: psutmwallyears__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__j ON public."PSUTMWAllYears" USING btree (j);


--
-- Name: psutmwallyears__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__laststage ON public."PSUTMWAllYears" USING btree ("LastStage");


--
-- Name: psutmwallyears__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__matname ON public."PSUTMWAllYears" USING btree (matname);


--
-- Name: psutmwallyears__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__method ON public."PSUTMWAllYears" USING btree ("Method");


--
-- Name: psutmwallyears__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__validfromversion ON public."PSUTMWAllYears" USING btree ("ValidFromVersion");


--
-- Name: psutmwallyears__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__validtoversion ON public."PSUTMWAllYears" USING btree ("ValidToVersion");


--
-- Name: psutmwallyears__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwallyears__year ON public."PSUTMWAllYears" USING btree ("Year");


--
-- Name: psutmwenergy__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__country ON public."PSUTMWEnergy" USING btree ("Country");


--
-- Name: psutmwenergy__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__dataset ON public."PSUTMWEnergy" USING btree ("Dataset");


--
-- Name: psutmwenergy__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__energytype ON public."PSUTMWEnergy" USING btree ("EnergyType");


--
-- Name: psutmwenergy__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__i ON public."PSUTMWEnergy" USING btree (i);


--
-- Name: psutmwenergy__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__j ON public."PSUTMWEnergy" USING btree (j);


--
-- Name: psutmwenergy__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__laststage ON public."PSUTMWEnergy" USING btree ("LastStage");


--
-- Name: psutmwenergy__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__matname ON public."PSUTMWEnergy" USING btree (matname);


--
-- Name: psutmwenergy__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__method ON public."PSUTMWEnergy" USING btree ("Method");


--
-- Name: psutmwenergy__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__validfromversion ON public."PSUTMWEnergy" USING btree ("ValidFromVersion");


--
-- Name: psutmwenergy__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__validtoversion ON public."PSUTMWEnergy" USING btree ("ValidToVersion");


--
-- Name: psutmwenergy__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutmwenergy__year ON public."PSUTMWEnergy" USING btree ("Year");


--
-- Name: psutreall__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__country ON public."PSUTReAll" USING btree ("Country");


--
-- Name: psutreall__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__dataset ON public."PSUTReAll" USING btree ("Dataset");


--
-- Name: psutreall__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__energytype ON public."PSUTReAll" USING btree ("EnergyType");


--
-- Name: psutreall__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__i ON public."PSUTReAll" USING btree (i);


--
-- Name: psutreall__includesneu; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__includesneu ON public."PSUTReAll" USING btree ("IncludesNEU");


--
-- Name: psutreall__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__j ON public."PSUTReAll" USING btree (j);


--
-- Name: psutreall__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__laststage ON public."PSUTReAll" USING btree ("LastStage");


--
-- Name: psutreall__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__matname ON public."PSUTReAll" USING btree (matname);


--
-- Name: psutreall__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__method ON public."PSUTReAll" USING btree ("Method");


--
-- Name: psutreall__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__validfromversion ON public."PSUTReAll" USING btree ("ValidFromVersion");


--
-- Name: psutreall__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__validtoversion ON public."PSUTReAll" USING btree ("ValidToVersion");


--
-- Name: psutreall__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreall__year ON public."PSUTReAll" USING btree ("Year");


--
-- Name: psutreallchopalldsallgrall__choppedmat; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__choppedmat ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("ChoppedMat");


--
-- Name: psutreallchopalldsallgrall__choppedvar; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__choppedvar ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("ChoppedVar");


--
-- Name: psutreallchopalldsallgrall__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__country ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("Country");


--
-- Name: psutreallchopalldsallgrall__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__dataset ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("Dataset");


--
-- Name: psutreallchopalldsallgrall__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__energytype ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("EnergyType");


--
-- Name: psutreallchopalldsallgrall__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__i ON public."PSUTReAllChopAllDsAllGrAll" USING btree (i);


--
-- Name: psutreallchopalldsallgrall__includesneu; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__includesneu ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("IncludesNEU");


--
-- Name: psutreallchopalldsallgrall__industryaggregation; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__industryaggregation ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("IndustryAggregation");


--
-- Name: psutreallchopalldsallgrall__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__j ON public."PSUTReAllChopAllDsAllGrAll" USING btree (j);


--
-- Name: psutreallchopalldsallgrall__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__laststage ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("LastStage");


--
-- Name: psutreallchopalldsallgrall__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__matname ON public."PSUTReAllChopAllDsAllGrAll" USING btree (matname);


--
-- Name: psutreallchopalldsallgrall__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__method ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("Method");


--
-- Name: psutreallchopalldsallgrall__productaggregation; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__productaggregation ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("ProductAggregation");


--
-- Name: psutreallchopalldsallgrall__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__validfromversion ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("ValidFromVersion");


--
-- Name: psutreallchopalldsallgrall__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__validtoversion ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("ValidToVersion");


--
-- Name: psutreallchopalldsallgrall__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutreallchopalldsallgrall__year ON public."PSUTReAllChopAllDsAllGrAll" USING btree ("Year");


--
-- Name: psutusefuliea__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__country ON public."PSUTUsefulIEA" USING btree ("Country");


--
-- Name: psutusefuliea__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__dataset ON public."PSUTUsefulIEA" USING btree ("Dataset");


--
-- Name: psutusefuliea__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__energytype ON public."PSUTUsefulIEA" USING btree ("EnergyType");


--
-- Name: psutusefuliea__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__i ON public."PSUTUsefulIEA" USING btree (i);


--
-- Name: psutusefuliea__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__j ON public."PSUTUsefulIEA" USING btree (j);


--
-- Name: psutusefuliea__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__laststage ON public."PSUTUsefulIEA" USING btree ("LastStage");


--
-- Name: psutusefuliea__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__matname ON public."PSUTUsefulIEA" USING btree (matname);


--
-- Name: psutusefuliea__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__method ON public."PSUTUsefulIEA" USING btree ("Method");


--
-- Name: psutusefuliea__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__validfromversion ON public."PSUTUsefulIEA" USING btree ("ValidFromVersion");


--
-- Name: psutusefuliea__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__validtoversion ON public."PSUTUsefulIEA" USING btree ("ValidToVersion");


--
-- Name: psutusefuliea__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefuliea__year ON public."PSUTUsefulIEA" USING btree ("Year");


--
-- Name: psutusefulieawithdetails__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__country ON public."PSUTUsefulIEAWithDetails" USING btree ("Country");


--
-- Name: psutusefulieawithdetails__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__dataset ON public."PSUTUsefulIEAWithDetails" USING btree ("Dataset");


--
-- Name: psutusefulieawithdetails__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__energytype ON public."PSUTUsefulIEAWithDetails" USING btree ("EnergyType");


--
-- Name: psutusefulieawithdetails__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__i ON public."PSUTUsefulIEAWithDetails" USING btree (i);


--
-- Name: psutusefulieawithdetails__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__j ON public."PSUTUsefulIEAWithDetails" USING btree (j);


--
-- Name: psutusefulieawithdetails__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__laststage ON public."PSUTUsefulIEAWithDetails" USING btree ("LastStage");


--
-- Name: psutusefulieawithdetails__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__matname ON public."PSUTUsefulIEAWithDetails" USING btree (matname);


--
-- Name: psutusefulieawithdetails__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__method ON public."PSUTUsefulIEAWithDetails" USING btree ("Method");


--
-- Name: psutusefulieawithdetails__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__validfromversion ON public."PSUTUsefulIEAWithDetails" USING btree ("ValidFromVersion");


--
-- Name: psutusefulieawithdetails__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__validtoversion ON public."PSUTUsefulIEAWithDetails" USING btree ("ValidToVersion");


--
-- Name: psutusefulieawithdetails__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutusefulieawithdetails__year ON public."PSUTUsefulIEAWithDetails" USING btree ("Year");


--
-- Name: psutwithneu__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__country ON public."PSUTWithNEU" USING btree ("Country");


--
-- Name: psutwithneu__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__dataset ON public."PSUTWithNEU" USING btree ("Dataset");


--
-- Name: psutwithneu__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__energytype ON public."PSUTWithNEU" USING btree ("EnergyType");


--
-- Name: psutwithneu__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__i ON public."PSUTWithNEU" USING btree (i);


--
-- Name: psutwithneu__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__j ON public."PSUTWithNEU" USING btree (j);


--
-- Name: psutwithneu__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__laststage ON public."PSUTWithNEU" USING btree ("LastStage");


--
-- Name: psutwithneu__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__matname ON public."PSUTWithNEU" USING btree (matname);


--
-- Name: psutwithneu__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__method ON public."PSUTWithNEU" USING btree ("Method");


--
-- Name: psutwithneu__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__validfromversion ON public."PSUTWithNEU" USING btree ("ValidFromVersion");


--
-- Name: psutwithneu__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__validtoversion ON public."PSUTWithNEU" USING btree ("ValidToVersion");


--
-- Name: psutwithneu__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithneu__year ON public."PSUTWithNEU" USING btree ("Year");


--
-- Name: psutwithoutneu__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__country ON public."PSUTWithoutNEU" USING btree ("Country");


--
-- Name: psutwithoutneu__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__dataset ON public."PSUTWithoutNEU" USING btree ("Dataset");


--
-- Name: psutwithoutneu__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__energytype ON public."PSUTWithoutNEU" USING btree ("EnergyType");


--
-- Name: psutwithoutneu__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__i ON public."PSUTWithoutNEU" USING btree (i);


--
-- Name: psutwithoutneu__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__j ON public."PSUTWithoutNEU" USING btree (j);


--
-- Name: psutwithoutneu__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__laststage ON public."PSUTWithoutNEU" USING btree ("LastStage");


--
-- Name: psutwithoutneu__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__matname ON public."PSUTWithoutNEU" USING btree (matname);


--
-- Name: psutwithoutneu__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__method ON public."PSUTWithoutNEU" USING btree ("Method");


--
-- Name: psutwithoutneu__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__validfromversion ON public."PSUTWithoutNEU" USING btree ("ValidFromVersion");


--
-- Name: psutwithoutneu__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__validtoversion ON public."PSUTWithoutNEU" USING btree ("ValidToVersion");


--
-- Name: psutwithoutneu__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX psutwithoutneu__year ON public."PSUTWithoutNEU" USING btree ("Year");


--
-- Name: sectoraggetafu__choppedmat; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__choppedmat ON public."SectorAggEtaFU" USING btree ("ChoppedMat");


--
-- Name: sectoraggetafu__choppedvar; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__choppedvar ON public."SectorAggEtaFU" USING btree ("ChoppedVar");


--
-- Name: sectoraggetafu__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__country ON public."SectorAggEtaFU" USING btree ("Country");


--
-- Name: sectoraggetafu__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__dataset ON public."SectorAggEtaFU" USING btree ("Dataset");


--
-- Name: sectoraggetafu__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__energytype ON public."SectorAggEtaFU" USING btree ("EnergyType");


--
-- Name: sectoraggetafu__grossnet; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__grossnet ON public."SectorAggEtaFU" USING btree ("GrossNet");


--
-- Name: sectoraggetafu__includesneu; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__includesneu ON public."SectorAggEtaFU" USING btree ("IncludesNEU");


--
-- Name: sectoraggetafu__industryaggregation; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__industryaggregation ON public."SectorAggEtaFU" USING btree ("IndustryAggregation");


--
-- Name: sectoraggetafu__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__method ON public."SectorAggEtaFU" USING btree ("Method");


--
-- Name: sectoraggetafu__productaggregation; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__productaggregation ON public."SectorAggEtaFU" USING btree ("ProductAggregation");


--
-- Name: sectoraggetafu__sector; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__sector ON public."SectorAggEtaFU" USING btree ("Sector");


--
-- Name: sectoraggetafu__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__validfromversion ON public."SectorAggEtaFU" USING btree ("ValidFromVersion");


--
-- Name: sectoraggetafu__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__validtoversion ON public."SectorAggEtaFU" USING btree ("ValidToVersion");


--
-- Name: sectoraggetafu__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX sectoraggetafu__year ON public."SectorAggEtaFU" USING btree ("Year");


--
-- Name: specifiedieadata__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__country ON public."SpecifiedIEAData" USING btree ("Country");


--
-- Name: specifiedieadata__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__dataset ON public."SpecifiedIEAData" USING btree ("Dataset");


--
-- Name: specifiedieadata__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__energytype ON public."SpecifiedIEAData" USING btree ("EnergyType");


--
-- Name: specifiedieadata__flow; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__flow ON public."SpecifiedIEAData" USING btree ("Flow");


--
-- Name: specifiedieadata__flowaggregationpoint; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__flowaggregationpoint ON public."SpecifiedIEAData" USING btree ("FlowAggregationPoint");


--
-- Name: specifiedieadata__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__laststage ON public."SpecifiedIEAData" USING btree ("LastStage");


--
-- Name: specifiedieadata__ledgerside; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__ledgerside ON public."SpecifiedIEAData" USING btree ("LedgerSide");


--
-- Name: specifiedieadata__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__method ON public."SpecifiedIEAData" USING btree ("Method");


--
-- Name: specifiedieadata__product; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__product ON public."SpecifiedIEAData" USING btree ("Product");


--
-- Name: specifiedieadata__unit; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__unit ON public."SpecifiedIEAData" USING btree ("Unit");


--
-- Name: specifiedieadata__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__validfromversion ON public."SpecifiedIEAData" USING btree ("ValidFromVersion");


--
-- Name: specifiedieadata__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__validtoversion ON public."SpecifiedIEAData" USING btree ("ValidToVersion");


--
-- Name: specifiedieadata__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX specifiedieadata__year ON public."SpecifiedIEAData" USING btree ("Year");


--
-- Name: yfuueioufudetails__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__country ON public."YfuUEIOUfudetails" USING btree ("Country");


--
-- Name: yfuueioufudetails__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__dataset ON public."YfuUEIOUfudetails" USING btree ("Dataset");


--
-- Name: yfuueioufudetails__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__energytype ON public."YfuUEIOUfudetails" USING btree ("EnergyType");


--
-- Name: yfuueioufudetails__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__i ON public."YfuUEIOUfudetails" USING btree (i);


--
-- Name: yfuueioufudetails__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__j ON public."YfuUEIOUfudetails" USING btree (j);


--
-- Name: yfuueioufudetails__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__laststage ON public."YfuUEIOUfudetails" USING btree ("LastStage");


--
-- Name: yfuueioufudetails__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__matname ON public."YfuUEIOUfudetails" USING btree (matname);


--
-- Name: yfuueioufudetails__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__method ON public."YfuUEIOUfudetails" USING btree ("Method");


--
-- Name: yfuueioufudetails__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__validfromversion ON public."YfuUEIOUfudetails" USING btree ("ValidFromVersion");


--
-- Name: yfuueioufudetails__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__validtoversion ON public."YfuUEIOUfudetails" USING btree ("ValidToVersion");


--
-- Name: yfuueioufudetails__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetails__year ON public."YfuUEIOUfudetails" USING btree ("Year");


--
-- Name: yfuueioufudetailsenergy__country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__country ON public."YfuUEIOUfudetailsEnergy" USING btree ("Country");


--
-- Name: yfuueioufudetailsenergy__dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__dataset ON public."YfuUEIOUfudetailsEnergy" USING btree ("Dataset");


--
-- Name: yfuueioufudetailsenergy__energytype; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__energytype ON public."YfuUEIOUfudetailsEnergy" USING btree ("EnergyType");


--
-- Name: yfuueioufudetailsenergy__i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__i ON public."YfuUEIOUfudetailsEnergy" USING btree (i);


--
-- Name: yfuueioufudetailsenergy__j; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__j ON public."YfuUEIOUfudetailsEnergy" USING btree (j);


--
-- Name: yfuueioufudetailsenergy__laststage; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__laststage ON public."YfuUEIOUfudetailsEnergy" USING btree ("LastStage");


--
-- Name: yfuueioufudetailsenergy__matname; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__matname ON public."YfuUEIOUfudetailsEnergy" USING btree (matname);


--
-- Name: yfuueioufudetailsenergy__method; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__method ON public."YfuUEIOUfudetailsEnergy" USING btree ("Method");


--
-- Name: yfuueioufudetailsenergy__validfromversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__validfromversion ON public."YfuUEIOUfudetailsEnergy" USING btree ("ValidFromVersion");


--
-- Name: yfuueioufudetailsenergy__validtoversion; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__validtoversion ON public."YfuUEIOUfudetailsEnergy" USING btree ("ValidToVersion");


--
-- Name: yfuueioufudetailsenergy__year; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX yfuueioufudetailsenergy__year ON public."YfuUEIOUfudetailsEnergy" USING btree ("Year");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_Sector_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_Sector_fkey" FOREIGN KEY ("Sector") REFERENCES public."Index"("IndexID");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_Species_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_Species_fkey" FOREIGN KEY ("Species") REFERENCES public."Species"("SpeciesID");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_Stage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_Stage_fkey" FOREIGN KEY ("Stage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_Unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_Unit_fkey" FOREIGN KEY ("Unit") REFERENCES public."Unit"("UnitID");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AMWPFUDataRaw AMWPFUDataRaw_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUDataRaw"
    ADD CONSTRAINT "AMWPFUDataRaw_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: AMWPFUData AMWPFUData_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: AMWPFUData AMWPFUData_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: AMWPFUData AMWPFUData_Sector_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_Sector_fkey" FOREIGN KEY ("Sector") REFERENCES public."Index"("IndexID");


--
-- Name: AMWPFUData AMWPFUData_Species_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_Species_fkey" FOREIGN KEY ("Species") REFERENCES public."Species"("SpeciesID");


--
-- Name: AMWPFUData AMWPFUData_Stage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_Stage_fkey" FOREIGN KEY ("Stage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: AMWPFUData AMWPFUData_Unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_Unit_fkey" FOREIGN KEY ("Unit") REFERENCES public."Unit"("UnitID");


--
-- Name: AMWPFUData AMWPFUData_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AMWPFUData AMWPFUData_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AMWPFUData AMWPFUData_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AMWPFUData"
    ADD CONSTRAINT "AMWPFUData_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: AggEtaPFU AggEtaPFU_ChoppedMat_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_ChoppedMat_fkey" FOREIGN KEY ("ChoppedMat") REFERENCES public.matname("matnameID");


--
-- Name: AggEtaPFU AggEtaPFU_ChoppedVar_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_ChoppedVar_fkey" FOREIGN KEY ("ChoppedVar") REFERENCES public."Index"("IndexID");


--
-- Name: AggEtaPFU AggEtaPFU_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: AggEtaPFU AggEtaPFU_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: AggEtaPFU AggEtaPFU_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: AggEtaPFU AggEtaPFU_GrossNet_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_GrossNet_fkey" FOREIGN KEY ("GrossNet") REFERENCES public."GrossNet"("GrossNetID");


--
-- Name: AggEtaPFU AggEtaPFU_IncludesNEU_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_IncludesNEU_fkey" FOREIGN KEY ("IncludesNEU") REFERENCES public."IncludesNEU"("IncludesNEUID");


--
-- Name: AggEtaPFU AggEtaPFU_IndustryAggregation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_IndustryAggregation_fkey" FOREIGN KEY ("IndustryAggregation") REFERENCES public."AggLevel"("AggLevelID");


--
-- Name: AggEtaPFU AggEtaPFU_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: AggEtaPFU AggEtaPFU_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: AggEtaPFU AggEtaPFU_ProductAggregation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_ProductAggregation_fkey" FOREIGN KEY ("ProductAggregation") REFERENCES public."AggLevel"("AggLevelID");


--
-- Name: AggEtaPFU AggEtaPFU_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AggEtaPFU AggEtaPFU_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AggEtaPFU AggEtaPFU_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AggEtaPFU"
    ADD CONSTRAINT "AggEtaPFU_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: AllIEAData AllIEAData_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: AllIEAData AllIEAData_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: AllIEAData AllIEAData_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: AllIEAData AllIEAData_FlowAggregationPoint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_FlowAggregationPoint_fkey" FOREIGN KEY ("FlowAggregationPoint") REFERENCES public."IEAFlowAggregationPoint"("IEAFlowAggregationPointID");


--
-- Name: AllIEAData AllIEAData_Flow_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_Flow_fkey" FOREIGN KEY ("Flow") REFERENCES public."Index"("IndexID");


--
-- Name: AllIEAData AllIEAData_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: AllIEAData AllIEAData_LedgerSide_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_LedgerSide_fkey" FOREIGN KEY ("LedgerSide") REFERENCES public."IEALedgerSide"("IEALedgerSideID");


--
-- Name: AllIEAData AllIEAData_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: AllIEAData AllIEAData_Product_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_Product_fkey" FOREIGN KEY ("Product") REFERENCES public."Index"("IndexID");


--
-- Name: AllIEAData AllIEAData_Unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_Unit_fkey" FOREIGN KEY ("Unit") REFERENCES public."Unit"("UnitID");


--
-- Name: AllIEAData AllIEAData_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AllIEAData AllIEAData_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AllIEAData AllIEAData_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllIEAData"
    ADD CONSTRAINT "AllIEAData_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: AllMachineData AllMachineData_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: AllMachineData AllMachineData_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: AllMachineData AllMachineData_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: AllMachineData AllMachineData_EuProduct_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_EuProduct_fkey" FOREIGN KEY ("EuProduct") REFERENCES public."Index"("IndexID");


--
-- Name: AllMachineData AllMachineData_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: AllMachineData AllMachineData_Machine_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_Machine_fkey" FOREIGN KEY ("Machine") REFERENCES public."Index"("IndexID");


--
-- Name: AllMachineData AllMachineData_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: AllMachineData AllMachineData_Quantity_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_Quantity_fkey" FOREIGN KEY ("Quantity") REFERENCES public."Quantity"("QuantityID");


--
-- Name: AllMachineData AllMachineData_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AllMachineData AllMachineData_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: AllMachineData AllMachineData_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."AllMachineData"
    ADD CONSTRAINT "AllMachineData_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: BalancedIEAData BalancedIEAData_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: BalancedIEAData BalancedIEAData_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: BalancedIEAData BalancedIEAData_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: BalancedIEAData BalancedIEAData_FlowAggregationPoint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_FlowAggregationPoint_fkey" FOREIGN KEY ("FlowAggregationPoint") REFERENCES public."IEAFlowAggregationPoint"("IEAFlowAggregationPointID");


--
-- Name: BalancedIEAData BalancedIEAData_Flow_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_Flow_fkey" FOREIGN KEY ("Flow") REFERENCES public."Index"("IndexID");


--
-- Name: BalancedIEAData BalancedIEAData_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: BalancedIEAData BalancedIEAData_LedgerSide_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_LedgerSide_fkey" FOREIGN KEY ("LedgerSide") REFERENCES public."IEALedgerSide"("IEALedgerSideID");


--
-- Name: BalancedIEAData BalancedIEAData_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: BalancedIEAData BalancedIEAData_Product_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_Product_fkey" FOREIGN KEY ("Product") REFERENCES public."Index"("IndexID");


--
-- Name: BalancedIEAData BalancedIEAData_Unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_Unit_fkey" FOREIGN KEY ("Unit") REFERENCES public."Unit"("UnitID");


--
-- Name: BalancedIEAData BalancedIEAData_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: BalancedIEAData BalancedIEAData_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: BalancedIEAData BalancedIEAData_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."BalancedIEAData"
    ADD CONSTRAINT "BalancedIEAData_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: CmatsAgg CmatsAgg_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: CmatsAgg CmatsAgg_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: CmatsAgg CmatsAgg_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: CmatsAgg CmatsAgg_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: CmatsAgg CmatsAgg_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: CmatsAgg CmatsAgg_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: CmatsAgg CmatsAgg_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: CmatsAgg CmatsAgg_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: CmatsAgg CmatsAgg_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: CmatsAgg CmatsAgg_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: CmatsAgg CmatsAgg_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CmatsAgg"
    ADD CONSTRAINT "CmatsAgg_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: Cmats Cmats_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: Cmats Cmats_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: Cmats Cmats_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: Cmats Cmats_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: Cmats Cmats_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: Cmats Cmats_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Cmats Cmats_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Cmats Cmats_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: Cmats Cmats_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: Cmats Cmats_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: Cmats Cmats_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Cmats"
    ADD CONSTRAINT "Cmats_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_CSource_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_CSource_fkey" FOREIGN KEY ("CSource") REFERENCES public."Country"("CountryID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_Destination_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_Destination_fkey" FOREIGN KEY ("Destination") REFERENCES public."Index"("IndexID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_EfProduct_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_EfProduct_fkey" FOREIGN KEY ("EfProduct") REFERENCES public."Index"("IndexID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_EuProduct_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_EuProduct_fkey" FOREIGN KEY ("EuProduct") REFERENCES public."Index"("IndexID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_FlowAggregationPoint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_FlowAggregationPoint_fkey" FOREIGN KEY ("FlowAggregationPoint") REFERENCES public."IEAFlowAggregationPoint"("IEAFlowAggregationPointID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_LedgerSide_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_LedgerSide_fkey" FOREIGN KEY ("LedgerSide") REFERENCES public."IEALedgerSide"("IEALedgerSideID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_Machine_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_Machine_fkey" FOREIGN KEY ("Machine") REFERENCES public."Index"("IndexID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_Quantity_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_Quantity_fkey" FOREIGN KEY ("Quantity") REFERENCES public."Quantity"("QuantityID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: CompletedAllocationTables CompletedAllocationTables_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedAllocationTables"
    ADD CONSTRAINT "CompletedAllocationTables_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_EuProduct_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_EuProduct_fkey" FOREIGN KEY ("EuProduct") REFERENCES public."Index"("IndexID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_Machine_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_Machine_fkey" FOREIGN KEY ("Machine") REFERENCES public."Index"("IndexID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_Quantity_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_Quantity_fkey" FOREIGN KEY ("Quantity") REFERENCES public."Quantity"("QuantityID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: CompletedEfficiencyTables CompletedEfficiencyTables_etafuSource_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedEfficiencyTables"
    ADD CONSTRAINT "CompletedEfficiencyTables_etafuSource_fkey" FOREIGN KEY ("etafuSource") REFERENCES public."Country"("CountryID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_EuProduct_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_EuProduct_fkey" FOREIGN KEY ("EuProduct") REFERENCES public."Index"("IndexID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_Machine_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_Machine_fkey" FOREIGN KEY ("Machine") REFERENCES public."Index"("IndexID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_PhiSource_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_PhiSource_fkey" FOREIGN KEY ("PhiSource") REFERENCES public."PhiSource"("PhiSourceID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_Quantity_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_Quantity_fkey" FOREIGN KEY ("Quantity") REFERENCES public."Quantity"("QuantityID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: CompletedPhiuTables CompletedPhiuTables_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."CompletedPhiuTables"
    ADD CONSTRAINT "CompletedPhiuTables_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: EtafuPhiuvecs EtafuPhiuvecs_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuPhiuvecs"
    ADD CONSTRAINT "EtafuPhiuvecs_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: EtafuYEIOU EtafuYEIOU_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: EtafuYEIOU EtafuYEIOU_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: EtafuYEIOU EtafuYEIOU_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: EtafuYEIOU EtafuYEIOU_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: EtafuYEIOU EtafuYEIOU_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: EtafuYEIOU EtafuYEIOU_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: EtafuYEIOU EtafuYEIOU_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: EtafuYEIOU EtafuYEIOU_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: EtafuYEIOU EtafuYEIOU_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: EtafuYEIOU EtafuYEIOU_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: EtafuYEIOU EtafuYEIOU_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOU"
    ADD CONSTRAINT "EtafuYEIOU_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: EtafuYEIOUagg EtafuYEIOUagg_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EtafuYEIOUagg"
    ADD CONSTRAINT "EtafuYEIOUagg_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: Etafuvecs Etafuvecs_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: Etafuvecs Etafuvecs_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: Etafuvecs Etafuvecs_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: Etafuvecs Etafuvecs_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: Etafuvecs Etafuvecs_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: Etafuvecs Etafuvecs_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Etafuvecs Etafuvecs_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Etafuvecs Etafuvecs_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: Etafuvecs Etafuvecs_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: Etafuvecs Etafuvecs_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: Etafuvecs Etafuvecs_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etafuvecs"
    ADD CONSTRAINT "Etafuvecs_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: Etai Etai_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: Etai Etai_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: Etai Etai_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: Etai Etai_IncludesNEU_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_IncludesNEU_fkey" FOREIGN KEY ("IncludesNEU") REFERENCES public."IncludesNEU"("IncludesNEUID");


--
-- Name: Etai Etai_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: Etai Etai_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: Etai Etai_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Etai Etai_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Etai Etai_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: Etai Etai_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: Etai Etai_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: Etai Etai_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Etai"
    ADD CONSTRAINT "Etai_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_Sector_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_Sector_fkey" FOREIGN KEY ("Sector") REFERENCES public."Index"("IndexID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_Species_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_Species_fkey" FOREIGN KEY ("Species") REFERENCES public."Species"("SpeciesID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_Stage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_Stage_fkey" FOREIGN KEY ("Stage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_Unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_Unit_fkey" FOREIGN KEY ("Unit") REFERENCES public."Unit"("UnitID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: HMWPFUDataRaw HMWPFUDataRaw_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUDataRaw"
    ADD CONSTRAINT "HMWPFUDataRaw_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: HMWPFUData HMWPFUData_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: HMWPFUData HMWPFUData_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: HMWPFUData HMWPFUData_Sector_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_Sector_fkey" FOREIGN KEY ("Sector") REFERENCES public."Index"("IndexID");


--
-- Name: HMWPFUData HMWPFUData_Species_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_Species_fkey" FOREIGN KEY ("Species") REFERENCES public."Species"("SpeciesID");


--
-- Name: HMWPFUData HMWPFUData_Stage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_Stage_fkey" FOREIGN KEY ("Stage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: HMWPFUData HMWPFUData_Unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_Unit_fkey" FOREIGN KEY ("Unit") REFERENCES public."Unit"("UnitID");


--
-- Name: HMWPFUData HMWPFUData_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: HMWPFUData HMWPFUData_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: HMWPFUData HMWPFUData_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."HMWPFUData"
    ADD CONSTRAINT "HMWPFUData_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: IEAData IEAData_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: IEAData IEAData_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: IEAData IEAData_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: IEAData IEAData_FlowAggregationPoint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_FlowAggregationPoint_fkey" FOREIGN KEY ("FlowAggregationPoint") REFERENCES public."IEAFlowAggregationPoint"("IEAFlowAggregationPointID");


--
-- Name: IEAData IEAData_Flow_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_Flow_fkey" FOREIGN KEY ("Flow") REFERENCES public."Index"("IndexID");


--
-- Name: IEAData IEAData_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: IEAData IEAData_LedgerSide_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_LedgerSide_fkey" FOREIGN KEY ("LedgerSide") REFERENCES public."IEALedgerSide"("IEALedgerSideID");


--
-- Name: IEAData IEAData_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: IEAData IEAData_Product_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_Product_fkey" FOREIGN KEY ("Product") REFERENCES public."Index"("IndexID");


--
-- Name: IEAData IEAData_Unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_Unit_fkey" FOREIGN KEY ("Unit") REFERENCES public."Unit"("UnitID");


--
-- Name: IEAData IEAData_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: IEAData IEAData_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: IEAData IEAData_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IEAData"
    ADD CONSTRAINT "IEAData_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_Destination_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_Destination_fkey" FOREIGN KEY ("Destination") REFERENCES public."Index"("IndexID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_EfProduct_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_EfProduct_fkey" FOREIGN KEY ("EfProduct") REFERENCES public."Index"("IndexID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_EuProduct_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_EuProduct_fkey" FOREIGN KEY ("EuProduct") REFERENCES public."Index"("IndexID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_FlowAggregationPoint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_FlowAggregationPoint_fkey" FOREIGN KEY ("FlowAggregationPoint") REFERENCES public."IEAFlowAggregationPoint"("IEAFlowAggregationPointID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_LedgerSide_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_LedgerSide_fkey" FOREIGN KEY ("LedgerSide") REFERENCES public."IEALedgerSide"("IEALedgerSideID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_Machine_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_Machine_fkey" FOREIGN KEY ("Machine") REFERENCES public."Index"("IndexID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_Quantity_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_Quantity_fkey" FOREIGN KEY ("Quantity") REFERENCES public."Quantity"("QuantityID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: IncompleteAllocationTables IncompleteAllocationTables_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."IncompleteAllocationTables"
    ADD CONSTRAINT "IncompleteAllocationTables_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: MachineData MachineData_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: MachineData MachineData_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: MachineData MachineData_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: MachineData MachineData_EuProduct_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_EuProduct_fkey" FOREIGN KEY ("EuProduct") REFERENCES public."Index"("IndexID");


--
-- Name: MachineData MachineData_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: MachineData MachineData_Machine_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_Machine_fkey" FOREIGN KEY ("Machine") REFERENCES public."Index"("IndexID");


--
-- Name: MachineData MachineData_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: MachineData MachineData_Quantity_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_Quantity_fkey" FOREIGN KEY ("Quantity") REFERENCES public."Quantity"("QuantityID");


--
-- Name: MachineData MachineData_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: MachineData MachineData_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: MachineData MachineData_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."MachineData"
    ADD CONSTRAINT "MachineData_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTFinalIEA PSUTFinalIEA_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTFinalIEA"
    ADD CONSTRAINT "PSUTFinalIEA_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTIEAMW PSUTIEAMW_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTIEAMW PSUTIEAMW_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTIEAMW PSUTIEAMW_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTIEAMW PSUTIEAMW_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTIEAMW PSUTIEAMW_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTIEAMW PSUTIEAMW_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTIEAMW PSUTIEAMW_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTIEAMW PSUTIEAMW_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTIEAMW PSUTIEAMW_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTIEAMW PSUTIEAMW_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTIEAMW PSUTIEAMW_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEAMW"
    ADD CONSTRAINT "PSUTIEAMW_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTIEA PSUTIEA_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTIEA PSUTIEA_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTIEA PSUTIEA_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTIEA PSUTIEA_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTIEA PSUTIEA_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTIEA PSUTIEA_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTIEA PSUTIEA_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTIEA PSUTIEA_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTIEA PSUTIEA_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTIEA PSUTIEA_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTIEA PSUTIEA_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTIEA"
    ADD CONSTRAINT "PSUTIEA_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTMWAllYears PSUTMWAllYears_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWAllYears"
    ADD CONSTRAINT "PSUTMWAllYears_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTMWEnergy PSUTMWEnergy_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMWEnergy"
    ADD CONSTRAINT "PSUTMWEnergy_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTMW PSUTMW_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTMW PSUTMW_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTMW PSUTMW_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTMW PSUTMW_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTMW PSUTMW_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTMW PSUTMW_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTMW PSUTMW_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTMW PSUTMW_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTMW PSUTMW_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTMW PSUTMW_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTMW PSUTMW_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTMW"
    ADD CONSTRAINT "PSUTMW_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_ChoppedMat_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_ChoppedMat_fkey" FOREIGN KEY ("ChoppedMat") REFERENCES public.matname("matnameID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_ChoppedVar_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_ChoppedVar_fkey" FOREIGN KEY ("ChoppedVar") REFERENCES public."Index"("IndexID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_IncludesNEU_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_IncludesNEU_fkey" FOREIGN KEY ("IncludesNEU") REFERENCES public."IncludesNEU"("IncludesNEUID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_IndustryAggregation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_IndustryAggregation_fkey" FOREIGN KEY ("IndustryAggregation") REFERENCES public."AggLevel"("AggLevelID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_ProductAggregation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_ProductAggregation_fkey" FOREIGN KEY ("ProductAggregation") REFERENCES public."AggLevel"("AggLevelID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTReAllChopAllDsAllGrAll PSUTReAllChopAllDsAllGrAll_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAllChopAllDsAllGrAll"
    ADD CONSTRAINT "PSUTReAllChopAllDsAllGrAll_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTReAll PSUTReAll_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTReAll PSUTReAll_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTReAll PSUTReAll_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTReAll PSUTReAll_IncludesNEU_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_IncludesNEU_fkey" FOREIGN KEY ("IncludesNEU") REFERENCES public."IncludesNEU"("IncludesNEUID");


--
-- Name: PSUTReAll PSUTReAll_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTReAll PSUTReAll_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTReAll PSUTReAll_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTReAll PSUTReAll_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTReAll PSUTReAll_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTReAll PSUTReAll_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTReAll PSUTReAll_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTReAll PSUTReAll_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTReAll"
    ADD CONSTRAINT "PSUTReAll_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTUsefulIEAWithDetails PSUTUsefulIEAWithDetails_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEAWithDetails"
    ADD CONSTRAINT "PSUTUsefulIEAWithDetails_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTUsefulIEA PSUTUsefulIEA_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTUsefulIEA"
    ADD CONSTRAINT "PSUTUsefulIEA_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTWithNEU PSUTWithNEU_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTWithNEU PSUTWithNEU_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTWithNEU PSUTWithNEU_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTWithNEU PSUTWithNEU_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTWithNEU PSUTWithNEU_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTWithNEU PSUTWithNEU_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTWithNEU PSUTWithNEU_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTWithNEU PSUTWithNEU_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTWithNEU PSUTWithNEU_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTWithNEU PSUTWithNEU_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTWithNEU PSUTWithNEU_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithNEU"
    ADD CONSTRAINT "PSUTWithNEU_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUTWithoutNEU PSUTWithoutNEU_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUTWithoutNEU"
    ADD CONSTRAINT "PSUTWithoutNEU_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PSUT PSUT_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PSUT PSUT_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PSUT PSUT_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: PSUT PSUT_IncludesNEU_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_IncludesNEU_fkey" FOREIGN KEY ("IncludesNEU") REFERENCES public."IncludesNEU"("IncludesNEUID");


--
-- Name: PSUT PSUT_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: PSUT PSUT_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: PSUT PSUT_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUT PSUT_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PSUT PSUT_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PSUT PSUT_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PSUT PSUT_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PSUT PSUT_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PSUT"
    ADD CONSTRAINT "PSUT_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PhiConstants PhiConstants_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhiConstants"
    ADD CONSTRAINT "PhiConstants_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PhiConstants PhiConstants_Product_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhiConstants"
    ADD CONSTRAINT "PhiConstants_Product_fkey" FOREIGN KEY ("Product") REFERENCES public."Index"("IndexID");


--
-- Name: PhiConstants PhiConstants_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhiConstants"
    ADD CONSTRAINT "PhiConstants_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PhiConstants PhiConstants_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhiConstants"
    ADD CONSTRAINT "PhiConstants_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Phipfvecs Phipfvecs_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: Phipfvecs Phipfvecs_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: Phipfvecs Phipfvecs_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: Phipfvecs Phipfvecs_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: Phipfvecs Phipfvecs_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: Phipfvecs Phipfvecs_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Phipfvecs Phipfvecs_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Phipfvecs Phipfvecs_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: Phipfvecs Phipfvecs_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: Phipfvecs Phipfvecs_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: Phipfvecs Phipfvecs_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phipfvecs"
    ADD CONSTRAINT "Phipfvecs_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: Phiuvecs Phiuvecs_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: Phiuvecs Phiuvecs_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: Phiuvecs Phiuvecs_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: Phiuvecs Phiuvecs_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: Phiuvecs Phiuvecs_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: Phiuvecs Phiuvecs_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Phiuvecs Phiuvecs_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Phiuvecs Phiuvecs_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: Phiuvecs Phiuvecs_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: Phiuvecs Phiuvecs_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: Phiuvecs Phiuvecs_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phiuvecs"
    ADD CONSTRAINT "Phiuvecs_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: PhivecsMW PhivecsMW_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: PhivecsMW PhivecsMW_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: PhivecsMW PhivecsMW_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PhivecsMW PhivecsMW_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: PhivecsMW PhivecsMW_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: PhivecsMW PhivecsMW_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: PhivecsMW PhivecsMW_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: PhivecsMW PhivecsMW_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PhivecsMW"
    ADD CONSTRAINT "PhivecsMW_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: Phivecs Phivecs_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: Phivecs Phivecs_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: Phivecs Phivecs_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Phivecs Phivecs_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: Phivecs Phivecs_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: Phivecs Phivecs_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: Phivecs Phivecs_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: Phivecs Phivecs_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Phivecs"
    ADD CONSTRAINT "Phivecs_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_ChoppedMat_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_ChoppedMat_fkey" FOREIGN KEY ("ChoppedMat") REFERENCES public.matname("matnameID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_ChoppedVar_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_ChoppedVar_fkey" FOREIGN KEY ("ChoppedVar") REFERENCES public."Index"("IndexID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_GrossNet_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_GrossNet_fkey" FOREIGN KEY ("GrossNet") REFERENCES public."GrossNet"("GrossNetID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_IncludesNEU_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_IncludesNEU_fkey" FOREIGN KEY ("IncludesNEU") REFERENCES public."IncludesNEU"("IncludesNEUID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_IndustryAggregation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_IndustryAggregation_fkey" FOREIGN KEY ("IndustryAggregation") REFERENCES public."AggLevel"("AggLevelID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_ProductAggregation_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_ProductAggregation_fkey" FOREIGN KEY ("ProductAggregation") REFERENCES public."AggLevel"("AggLevelID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_Sector_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_Sector_fkey" FOREIGN KEY ("Sector") REFERENCES public."Index"("IndexID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: SectorAggEtaFU SectorAggEtaFU_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SectorAggEtaFU"
    ADD CONSTRAINT "SectorAggEtaFU_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_FlowAggregationPoint_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_FlowAggregationPoint_fkey" FOREIGN KEY ("FlowAggregationPoint") REFERENCES public."IEAFlowAggregationPoint"("IEAFlowAggregationPointID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_Flow_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_Flow_fkey" FOREIGN KEY ("Flow") REFERENCES public."Index"("IndexID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_LedgerSide_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_LedgerSide_fkey" FOREIGN KEY ("LedgerSide") REFERENCES public."IEALedgerSide"("IEALedgerSideID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_Product_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_Product_fkey" FOREIGN KEY ("Product") REFERENCES public."Index"("IndexID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_Unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_Unit_fkey" FOREIGN KEY ("Unit") REFERENCES public."Unit"("UnitID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: SpecifiedIEAData SpecifiedIEAData_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."SpecifiedIEAData"
    ADD CONSTRAINT "SpecifiedIEAData_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: YfuUEIOUfudetailsEnergy YfuUEIOUfudetailsEnergy_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetailsEnergy"
    ADD CONSTRAINT "YfuUEIOUfudetailsEnergy_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_Country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_Country_fkey" FOREIGN KEY ("Country") REFERENCES public."Country"("CountryID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_Dataset_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_Dataset_fkey" FOREIGN KEY ("Dataset") REFERENCES public."Dataset"("DatasetID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_EnergyType_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_EnergyType_fkey" FOREIGN KEY ("EnergyType") REFERENCES public."EnergyType"("EnergyTypeID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_LastStage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_LastStage_fkey" FOREIGN KEY ("LastStage") REFERENCES public."ECCStage"("ECCStageID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_Method_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_Method_fkey" FOREIGN KEY ("Method") REFERENCES public."Method"("MethodID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_ValidFromVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_ValidFromVersion_fkey" FOREIGN KEY ("ValidFromVersion") REFERENCES public."Version"("VersionID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_ValidToVersion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_ValidToVersion_fkey" FOREIGN KEY ("ValidToVersion") REFERENCES public."Version"("VersionID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_Year_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_Year_fkey" FOREIGN KEY ("Year") REFERENCES public."Year"("YearID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_i_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_i_fkey" FOREIGN KEY (i) REFERENCES public."Index"("IndexID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_j_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_j_fkey" FOREIGN KEY (j) REFERENCES public."Index"("IndexID");


--
-- Name: YfuUEIOUfudetails YfuUEIOUfudetails_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."YfuUEIOUfudetails"
    ADD CONSTRAINT "YfuUEIOUfudetails_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: matnameRCType matnameRCType_coltype_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."matnameRCType"
    ADD CONSTRAINT "matnameRCType_coltype_fkey" FOREIGN KEY (coltype) REFERENCES public."RCType"("RCTypeID");


--
-- Name: matnameRCType matnameRCType_matname_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."matnameRCType"
    ADD CONSTRAINT "matnameRCType_matname_fkey" FOREIGN KEY (matname) REFERENCES public.matname("matnameID");


--
-- Name: matnameRCType matnameRCType_rowtype_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."matnameRCType"
    ADD CONSTRAINT "matnameRCType_rowtype_fkey" FOREIGN KEY (rowtype) REFERENCES public."RCType"("RCTypeID");


--
-- PostgreSQL database dump complete
--

\unrestrict kM8THnfXpEAyvNuMxOqEMBRJ2dQ0XGrxI5VRx8UJXuWm4OLxe37UNtw17TLD2w5

