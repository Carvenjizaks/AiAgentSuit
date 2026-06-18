"""
Generate Management Accounts and Odoo Migration data for
The Powerhouse Fellowship Trust – Feb to 16 Jun 2026
Source: Standard Bank Namibia statement, account 042746051
"""

import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# RAW TRANSACTIONS
# Each entry: (date YYYY-MM-DD, description, debit, credit, balance, reference)
# ---------------------------------------------------------------------------
TRANSACTIONS = [
    # ===== FEBRUARY 2026 =====
    ("2026-02-01", "Opening Balance", 0, 0, 89089.68, "OPEN"),
    ("2026-02-03", "IB PAYMENT FROM POWERHOUSE TITHE RRF 379", 0, 1362.00, 0, "EFT-IN"),
    ("2026-02-03", "IB PAYMENT FROM Tithe 379", 0, 2600.00, 0, "EFT-IN"),
    ("2026-02-03", "IB PAYMENT FROM HANSEN RAMON 379", 0, 5000.00, 0, "EFT-IN"),
    ("2026-02-04", "JM Izaks Tithe", 0, 1950.00, 0, "EFT-IN"),
    ("2026-02-04", "Bruce & Mary Hansen Tithe", 0, 12900.00, 0, "EFT-IN"),
    ("2026-02-04", "Bruce & Mary Hansen Offering", 0, 300.00, 0, "EFT-IN"),
    ("2026-02-05", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 5200.00, 0, "CASH-DEP"),
    ("2026-02-06", "E.B Strauss Tithe", 0, 6380.00, 0, "EFT-IN"),
    ("2026-02-06", "BWXXNAMIHP-NHP SUB Medical Aid", 17759.00, 0, 0, "DEBIT-ORDER"),
    ("2026-02-06", "BWXXSANLAM Insurance", 3382.77, 0, 0, "DEBIT-ORDER"),
    ("2026-02-06", "BWXXHOMEST-HS3785 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-02-06", "BWXXHOMEST-HS3890 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-02-07", "SIMONIS STORM Donation", 0, 10000.00, 0, "EFT-IN"),
    ("2026-02-09", "FNXXPARATU10008496 Internet Paratus", 1782.96, 0, 0, "DEBIT-ORDER"),
    ("2026-02-09", "FNXXMTC MTC Mobile", 362.00, 0, 0, "DEBIT-ORDER"),
    ("2026-02-09", "FNXXOMSICN616749242 City of Windhoek Utilities", 6423.00, 0, 0, "DEBIT-ORDER"),
    ("2026-02-09", "FNXXOMSICN607707170 City of Windhoek Utilities", 2826.00, 0, 0, "DEBIT-ORDER"),
    ("2026-02-10", "MLPAYMENT", 3618.68, 0, 0, "DEBIT-ORDER"),
    ("2026-02-10", "SBXXOMLACN Debit Order", 3521.27, 0, 0, "DEBIT-ORDER"),
    ("2026-02-10", "SBXXOMLACN Debit Order 2", 632.00, 0, 0, "DEBIT-ORDER"),
    ("2026-02-11", "Cash Deposit - M Izaks (Weekly tithe & offering)", 0, 7800.00, 0, "CASH-DEP"),
    ("2026-02-11", "ASTRIDO Tithe", 0, 10500.00, 0, "EFT-IN"),
    ("2026-02-11", "Rozan Malumo Tithe", 0, 6200.00, 0, "EFT-IN"),
    ("2026-02-11", "DE ALMEIDAS Contribution", 0, 2025.00, 0, "EFT-IN"),
    ("2026-02-12", "COURTYARD HOUS Hotel Accommodation", 374.00, 0, 0, "TRAVEL"),
    ("2026-02-13", "IB PAYMENT FROM ZANE CAREW 379", 0, 2500.00, 0, "EFT-IN"),
    ("2026-02-13", "IB PAYMENT FROM BERTHA NJEMBO 379", 0, 4300.00, 0, "EFT-IN"),
    ("2026-02-14", "PT20260214 Online Giving", 0, 1450.00, 0, "ONLINE-GIVING"),
    ("2026-02-16", "Simonis Storm Outgoing", 10000.00, 0, 0, "EFT-OUT"),
    ("2026-02-16", "ALLY MERCIA MAURIH Tithe", 0, 7885.00, 0, "EFT-IN"),
    ("2026-02-17", "Stop Order POWER HOUSE FELL 1009", 0, 1500.00, 0, "EFT-IN"),
    ("2026-02-17", "MS FLORA MUPIA Tithe", 0, 3013.00, 0, "EFT-IN"),
    ("2026-02-18", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 8400.00, 0, "CASH-DEP"),
    ("2026-02-18", "TMZ TITHE", 0, 8000.00, 0, "EFT-IN"),
    ("2026-02-18", "Shughaza tiende Tithe", 0, 4062.00, 0, "EFT-IN"),
    ("2026-02-18", "Tith Off Mr & Mrs Ngaveten Tithe", 0, 8300.00, 0, "EFT-IN"),
    ("2026-02-19", "COURTYARD Hotel Accommodation", 12759.00, 0, 0, "TRAVEL"),
    ("2026-02-19", "AGODA Accommodation booking", 2693.64, 0, 0, "TRAVEL"),
    ("2026-02-20", "BOL PAYMENT ASHLEYRENOVATI Renovation", 3250.00, 0, 0, "RENOVATION"),
    ("2026-02-20", "IB PAYMENT FROM ALAN amp LJ 10TH 379", 0, 11900.00, 0, "EFT-IN"),
    ("2026-02-20", "IB PAYMENT FROM TITHE 379", 0, 1400.00, 0, "EFT-IN"),
    ("2026-02-20", "SH Beukes Rivers MC26 Tithe", 0, 12500.00, 0, "EFT-IN"),
    ("2026-02-23", "Conville Britz Tithe", 0, 10350.00, 0, "EFT-IN"),
    ("2026-02-23", "Tithe Uazukuani", 0, 6200.00, 0, "EFT-IN"),
    ("2026-02-23", "Offering Uazukuani", 0, 100.00, 0, "EFT-IN"),
    ("2026-02-24", "BOL PAYMENT -SAL+EXPENPHOUSE Staff Salaries", 5900.00, 0, 0, "SALARIES"),
    ("2026-02-24", "Irene Oppel Tithe", 0, 2200.00, 0, "EFT-IN"),
    ("2026-02-25", "Cash Deposit - R Beukes (Weekly tithe & offering)", 0, 6300.00, 0, "CASH-DEP"),
    ("2026-02-25", "Lauren Tithe", 0, 4000.00, 0, "EFT-IN"),
    ("2026-02-25", "Grant Klein Tithe", 0, 2200.00, 0, "EFT-IN"),
    ("2026-02-25", "BEULAH Tithe", 0, 2000.00, 0, "EFT-IN"),
    ("2026-02-26", "Bank Charges BOL Monthly", 685.00, 0, 0, "BANK-CHARGES"),
    ("2026-02-26", "Debit order execution fees Feb", 299.70, 0, 0, "BANK-CHARGES"),
    ("2026-02-26", "Monthly management fee", 90.00, 0, 0, "BANK-CHARGES"),
    ("2026-02-26", "POS fees Feb", 80.00, 0, 0, "BANK-CHARGES"),
    ("2026-02-27", "Credit Interest", 0, 39.63, 0, "INTEREST"),
    ("2026-02-27", "BOL PAYMENT 0912MR. CARVEN J. I Carven Izaks", 2000.00, 0, 0, "SALARIES"),
    ("2026-02-27", "Engen Fuel", 650.00, 0, 0, "FUEL"),
    ("2026-02-27", "Woolworths Groceries", 850.00, 0, 0, "GROCERIES"),
    ("2026-02-27", "Checkers Groceries", 420.00, 0, 0, "GROCERIES"),
    ("2026-02-28", "FNXXMTC MTC Mobile Feb", 0, 0, 89048.57, "BALANCE"),

    # ===== MARCH 2026 =====
    ("2026-03-02", "IB PAYMENT FROM POWERHOUSE TITHE RRF 379", 0, 1362.00, 0, "EFT-IN"),
    ("2026-03-02", "IB PAYMENT FROM Tithe 379", 0, 2600.00, 0, "EFT-IN"),
    ("2026-03-02", "IB PAYMENT FROM HANSEN RAMON 379", 0, 5000.00, 0, "EFT-IN"),
    ("2026-03-03", "JM Izaks Tithe", 0, 1950.00, 0, "EFT-IN"),
    ("2026-03-03", "Bruce & Mary Hansen Tithe", 0, 12900.00, 0, "EFT-IN"),
    ("2026-03-03", "Bruce & Mary Hansen Offering", 0, 300.00, 0, "EFT-IN"),
    ("2026-03-03", "E.B Strauss Tithe", 0, 6600.00, 0, "EFT-IN"),
    ("2026-03-04", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 9200.00, 0, "CASH-DEP"),
    ("2026-03-04", "SIMONIS STORM Donation", 0, 30000.00, 0, "EFT-IN"),
    ("2026-03-05", "BWXXNAMIHP-NHP SUB Medical Aid", 17759.00, 0, 0, "DEBIT-ORDER"),
    ("2026-03-05", "BWXXSANLAM Insurance", 3382.77, 0, 0, "DEBIT-ORDER"),
    ("2026-03-05", "BWXXHOMEST-HS3785 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-03-05", "BWXXHOMEST-HS3890 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-03-06", "ASTRIDO Tithe", 0, 15000.00, 0, "EFT-IN"),
    ("2026-03-06", "DE ALMEIDAS Contribution", 0, 4025.00, 0, "EFT-IN"),
    ("2026-03-06", "Rozan Malumo Tithe", 0, 6500.00, 0, "EFT-IN"),
    ("2026-03-07", "FNXXPARATU10008496 Internet Paratus", 1782.96, 0, 0, "DEBIT-ORDER"),
    ("2026-03-07", "FNXXMTC MTC Mobile", 420.00, 0, 0, "DEBIT-ORDER"),
    ("2026-03-07", "FNXXOMSICN616749242 City of Windhoek Utilities", 6500.00, 0, 0, "DEBIT-ORDER"),
    ("2026-03-07", "FNXXOMSICN607707170 City of Windhoek Utilities", 2900.00, 0, 0, "DEBIT-ORDER"),
    ("2026-03-09", "MLPAYMENT", 13524.09, 0, 0, "DEBIT-ORDER"),
    ("2026-03-09", "AFPAYMENT", 13108.19, 0, 0, "DEBIT-ORDER"),
    ("2026-03-09", "SBXXOMLACN Debit Order", 3521.27, 0, 0, "DEBIT-ORDER"),
    ("2026-03-09", "SBXXOMLACN Debit Order 2", 632.00, 0, 0, "DEBIT-ORDER"),
    ("2026-03-10", "Stop Order POWER HOUSE FELL 1009", 0, 1500.00, 0, "EFT-IN"),
    ("2026-03-10", "MS FLORA MUPIA Tithe", 0, 3013.00, 0, "EFT-IN"),
    ("2026-03-10", "IB PAYMENT FROM ZANE CAREW 379", 0, 2800.00, 0, "EFT-IN"),
    ("2026-03-10", "IB PAYMENT FROM BERTHA NJEMBO 379", 0, 4300.00, 0, "EFT-IN"),
    ("2026-03-11", "Cash Deposit - M Izaks (Weekly tithe & offering)", 0, 11500.00, 0, "CASH-DEP"),
    ("2026-03-11", "BOL PAYMENT -SAL+EXPENPHOUSE-SAL EXPE Staff Salaries", 55000.00, 0, 0, "SALARIES"),
    ("2026-03-11", "Frikkie Jordaan Contractor", 11025.00, 0, 0, "CONTRACTORS"),
    ("2026-03-11", "Frikkie Jordaan Expenses", 820.61, 0, 0, "CONTRACTORS"),
    ("2026-03-11", "Scouts of Namibia Facility rental", 16000.00, 0, 0, "FACILITY-RENTAL"),
    ("2026-03-12", "IB PAYMENT FROM ALAN amp LJ 10TH 379", 0, 24000.00, 0, "EFT-IN"),
    ("2026-03-12", "IB PAYMENT FROM TITHE 379", 0, 1400.00, 0, "EFT-IN"),
    ("2026-03-12", "ALLY MERCIA MAURIH Tithe", 0, 1670.00, 0, "EFT-IN"),
    ("2026-03-13", "Windhoek Hi WHS School fees/sponsorship", 3500.00, 0, 0, "EDUCATION"),
    ("2026-03-13", "ANTHROPIC CLAUDE AI Subscription", 640.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "ANTHROPIC CLAUDE AI Subscription", 340.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "ANTHROPIC CLAUDE AI Subscription", 180.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "OPENAI CHATGPT Subscription", 1029.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "VERCEL DINOABLD Hosting", 1217.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "VERCEL MKT SUP Hosting", 1217.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "KIMI API PLATF AI Platform", 341.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "MOONSHOT AI PT AI Platform", 856.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "P SKOOL COM RX Online Learning", 293.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "WWW SCISPACE C Research Tools", 1493.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-13", "Google Workspace Subscription", 716.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-14", "JANSEN Tithe", 0, 14675.00, 0, "EFT-IN"),
    ("2026-03-14", "M Lubinda Mens Conf Conference Income", 0, 14500.00, 0, "CONFERENCE-INCOME"),
    ("2026-03-14", "Alan Hansen Sponsor Jhb Confer Sponsorship", 0, 10825.00, 0, "CONFERENCE-INCOME"),
    ("2026-03-14", "TMZ TITHE", 0, 5000.00, 0, "EFT-IN"),
    ("2026-03-15", "CVENT 74TH NA Conference registration", 10800.51, 0, 0, "TRAVEL"),
    ("2026-03-16", "Cash Deposit - R Beukes (Weekly tithe & offering)", 0, 14200.00, 0, "CASH-DEP"),
    ("2026-03-16", "IB PAYMENT FROM COLLIN VAN WYK 379", 0, 11000.00, 0, "EFT-IN"),
    ("2026-03-16", "Tith Off Mr & Mrs Ngaveten Tithe", 0, 7000.00, 0, "EFT-IN"),
    ("2026-03-16", "AMWELE TITHE Tithe", 0, 5000.00, 0, "EFT-IN"),
    ("2026-03-17", "Bravofly Flights", 39542.98, 0, 0, "TRAVEL"),
    ("2026-03-17", "BOL PAYMENT ASHLEYRENOVATI Renovation", 5500.00, 0, 0, "RENOVATION"),
    ("2026-03-17", "BOL PAYMENT Dr Schulze Contractor", 909.42, 0, 0, "CONTRACTORS"),
    ("2026-03-18", "Shughaza tiende Tithe", 0, 4062.00, 0, "EFT-IN"),
    ("2026-03-18", "Irene Oppel Tithe", 0, 3000.00, 0, "EFT-IN"),
    ("2026-03-18", "Lauren Tithe", 0, 5000.00, 0, "EFT-IN"),
    ("2026-03-18", "Tithe Uazukuani", 0, 6200.00, 0, "EFT-IN"),
    ("2026-03-18", "Offering Uazukuani", 0, 100.00, 0, "EFT-IN"),
    ("2026-03-18", "SH Beukes Rivers MC26 Tithe", 0, 12500.00, 0, "EFT-IN"),
    ("2026-03-18", "Conville Britz Tithe", 0, 10350.00, 0, "EFT-IN"),
    ("2026-03-18", "IB PAYMENT FROM POWERHOUSE TITHE RRF 379", 0, 1362.00, 0, "EFT-IN"),
    ("2026-03-18", "Pastor-Powehouse Offering", 0, 2000.00, 0, "EFT-IN"),
    ("2026-03-19", "Stage Audio World Equipment", 2309.20, 0, 0, "EQUIPMENT"),
    ("2026-03-20", "BOL PAYMENT Belinda Staff payment", 2718.00, 0, 0, "SALARIES"),
    ("2026-03-20", "BOL PAYMENT -SAL+EXPENPHOUSE-SAL EXPE Staff Salaries Mar", 5000.00, 0, 0, "SALARIES"),
    ("2026-03-20", "BOL PAYMENT 0912MR. CARVEN J. I Carven Izaks", 3864.00, 0, 0, "SALARIES"),
    ("2026-03-21", "PayFast Rivers Event Ticket", 2625.00, 0, 0, "EVENTS"),
    ("2026-03-21", "Apple Store Technology", 12959.34, 0, 0, "TECHNOLOGY"),
    ("2026-03-21", "Cotton On VA Clothing", 2201.00, 0, 0, "PERSONAL"),
    ("2026-03-22", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 17000.00, 0, "CASH-DEP"),
    ("2026-03-22", "PT20260322 Online Giving", 0, 2100.00, 0, "ONLINE-GIVING"),
    ("2026-03-23", "Booking.com Accommodation", 21018.45, 0, 0, "TRAVEL"),
    ("2026-03-23", "AMWELE Tithe", 0, 5000.00, 0, "EFT-IN"),
    ("2026-03-24", "VENICE AI Subscription", 425.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-24", "Ampleur Global Software", 336.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-24", "OpenRouter AI Platform", 182.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-25", "Bank Charges BOL Monthly Mar", 850.00, 0, 0, "BANK-CHARGES"),
    ("2026-03-25", "Debit order execution fees Mar", 399.60, 0, 0, "BANK-CHARGES"),
    ("2026-03-25", "Duty on debit entries Mar", 25.50, 0, 0, "BANK-CHARGES"),
    ("2026-03-26", "Woolworths Groceries", 1100.00, 0, 0, "GROCERIES"),
    ("2026-03-26", "Bootlegger Restaurant", 1800.00, 0, 0, "MEALS"),
    ("2026-03-26", "Engen Fuel", 850.00, 0, 0, "FUEL"),
    ("2026-03-27", "Dischem Pharmacy", 1091.00, 0, 0, "MEDICAL"),
    ("2026-03-27", "Credit Interest", 0, 47.99, 0, "INTEREST"),
    ("2026-03-28", "PAYPAL SMTP Hosting services", 650.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-28", "MAGAI AI Tool", 686.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-28", "Hyonix Hosting", 384.00, 0, 0, "TECHNOLOGY"),
    ("2026-03-30", "Barco Namibia Maintenance", 1082.44, 0, 0, "MAINTENANCE"),
    ("2026-03-31", "Balance Mar", 0, 0, 124472.28, "BALANCE"),

    # ===== APRIL 2026 =====
    ("2026-04-01", "IB PAYMENT FROM POWERHOUSE TITHE RRF 379", 0, 1364.00, 0, "EFT-IN"),
    ("2026-04-01", "IB PAYMENT FROM Tithe 379", 0, 2600.00, 0, "EFT-IN"),
    ("2026-04-01", "IB PAYMENT FROM HANSEN RAMON 379", 0, 5000.00, 0, "EFT-IN"),
    ("2026-04-01", "JM Izaks Tithe", 0, 1950.00, 0, "EFT-IN"),
    ("2026-04-01", "Bruce & Mary Hansen Tithe", 0, 12900.00, 0, "EFT-IN"),
    ("2026-04-01", "Bruce & Mary Hansen Offering", 0, 500.00, 0, "EFT-IN"),
    ("2026-04-02", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 13500.00, 0, "CASH-DEP"),
    ("2026-04-02", "SIMONIS STORM Donation", 0, 35000.00, 0, "EFT-IN"),
    ("2026-04-03", "BWXXNAMIHP-NHP SUB Medical Aid", 17759.00, 0, 0, "DEBIT-ORDER"),
    ("2026-04-03", "BWXXSANLAM Insurance", 3382.77, 0, 0, "DEBIT-ORDER"),
    ("2026-04-03", "BWXXHOMEST-HS3785 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-04-03", "BWXXHOMEST-HS3890 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-04-04", "E.B Strauss Tithe", 0, 6380.00, 0, "EFT-IN"),
    ("2026-04-04", "DE ALMEIDAS Contribution", 0, 9025.00, 0, "EFT-IN"),
    ("2026-04-04", "Rozan Malumo Tithe", 0, 6750.00, 0, "EFT-IN"),
    ("2026-04-04", "ASTRIDO Tithe", 0, 61000.00, 0, "EFT-IN"),
    ("2026-04-05", "FNXXPARATU10008496 Internet Paratus", 1782.96, 0, 0, "DEBIT-ORDER"),
    ("2026-04-05", "FNXXMTC MTC Mobile", 500.00, 0, 0, "DEBIT-ORDER"),
    ("2026-04-05", "FNXXOMSICN616749242 City of Windhoek Utilities", 6573.00, 0, 0, "DEBIT-ORDER"),
    ("2026-04-05", "FNXXOMSICN607707170 City of Windhoek Utilities", 2969.00, 0, 0, "DEBIT-ORDER"),
    ("2026-04-06", "MLPAYMENT", 13524.09, 0, 0, "DEBIT-ORDER"),
    ("2026-04-06", "AFPAYMENT", 13108.19, 0, 0, "DEBIT-ORDER"),
    ("2026-04-06", "SBXXOMLACN Debit Order", 3521.27, 0, 0, "DEBIT-ORDER"),
    ("2026-04-06", "SBXXOMLACN Debit Order 2", 632.00, 0, 0, "DEBIT-ORDER"),
    ("2026-04-07", "CJI-FNBPHOUSE-DISTRIBU Ministry Distribution", 20195.00, 0, 0, "MINISTRY-DIST"),
    ("2026-04-07", "CJI-FNBPHOUSE-DISTRIBU Ministry Distribution", 49590.00, 0, 0, "MINISTRY-DIST"),
    ("2026-04-07", "CJI-FNBPHOUSE-DISTRIBU Ministry Distribution", 15000.00, 0, 0, "MINISTRY-DIST"),
    ("2026-04-07", "Simonis Storm Outgoing", 10000.00, 0, 0, "EFT-OUT"),
    ("2026-04-08", "Stop Order POWER HOUSE FELL 1009", 0, 1500.00, 0, "EFT-IN"),
    ("2026-04-08", "MS FLORA MUPIA Tithe", 0, 3013.00, 0, "EFT-IN"),
    ("2026-04-08", "Cash Deposit - M Izaks (Weekly tithe & offering)", 0, 21500.00, 0, "CASH-DEP"),
    ("2026-04-08", "IB PAYMENT FROM ZANE CAREW 379", 0, 2800.00, 0, "EFT-IN"),
    ("2026-04-08", "IB PAYMENT FROM BERTHA NJEMBO 379", 0, 4300.00, 0, "EFT-IN"),
    ("2026-04-08", "AiTraining Powehouse-Refund Refund received", 0, 16628.60, 0, "REFUNDS"),
    ("2026-04-09", "Pastor-FF-MGM Management payment", 20000.00, 0, 0, "SALARIES"),
    ("2026-04-09", "Scouts of Namibia Facility rental", 8000.00, 0, 0, "FACILITY-RENTAL"),
    ("2026-04-10", "eDreams Flights", 10123.48, 0, 0, "TRAVEL"),
    ("2026-04-10", "Bravofly Flights", 7458.97, 0, 0, "TRAVEL"),
    ("2026-04-10", "BKG BOOKING CO Accommodation", 5050.89, 0, 0, "TRAVEL"),
    ("2026-04-10", "BKG BOOKING CO Accommodation", 4321.25, 0, 0, "TRAVEL"),
    ("2026-04-11", "TMZ TITHE", 0, 8000.00, 0, "EFT-IN"),
    ("2026-04-11", "ALLY MERCIA MAURIH Tithe", 0, 4300.00, 0, "EFT-IN"),
    ("2026-04-11", "JANSEN Tithe", 0, 14675.00, 0, "EFT-IN"),
    ("2026-04-11", "Shughaza tiende Tithe", 0, 4062.00, 0, "EFT-IN"),
    ("2026-04-13", "IB PAYMENT FROM ALAN amp LJ 10TH 379", 0, 24000.00, 0, "EFT-IN"),
    ("2026-04-13", "IB PAYMENT FROM TITHE 379", 0, 1400.00, 0, "EFT-IN"),
    ("2026-04-13", "Tith Off Mr & Mrs Ngaveten Tithe", 0, 8300.00, 0, "EFT-IN"),
    ("2026-04-13", "AMWELE Tithe", 0, 5000.00, 0, "EFT-IN"),
    ("2026-04-14", "BOL PAYMENT ASHLEYRENOVATI Renovation", 3600.00, 0, 0, "RENOVATION"),
    ("2026-04-14", "ANTHROPIC CLAUDE AI Subscription", 420.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-14", "ANTHROPIC CLAUDE AI Subscription", 210.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-14", "OPENAI CHATGPT Subscription", 780.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-14", "VERCEL DINOABLD Hosting", 322.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-14", "KIMI API PLATF AI Platform", 336.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-14", "MOONSHOT AI PT AI Platform", 162.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-14", "Google Workspace Subscription", 551.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-14", "WWW SCISPACE C Research Tools", 397.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-15", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 9800.00, 0, "CASH-DEP"),
    ("2026-04-15", "PT20260415 Online Giving", 0, 1800.00, 0, "ONLINE-GIVING"),
    ("2026-04-15", "SIMONIS STORM Donation", 0, 20000.00, 0, "EFT-IN"),
    ("2026-04-16", "Irene Oppel Tithe", 0, 2200.00, 0, "EFT-IN"),
    ("2026-04-16", "Lauren Tithe", 0, 4500.00, 0, "EFT-IN"),
    ("2026-04-16", "Conville Britz Tithe", 0, 10350.00, 0, "EFT-IN"),
    ("2026-04-16", "Tithe Uazukuani", 0, 6200.00, 0, "EFT-IN"),
    ("2026-04-16", "Offering Uazukuani", 0, 100.00, 0, "EFT-IN"),
    ("2026-04-16", "SH Beukes Rivers MC26 Tithe", 0, 12500.00, 0, "EFT-IN"),
    ("2026-04-17", "JAQS Eros Office Rental Refund", 0, 1365.40, 0, "REFUNDS"),
    ("2026-04-18", "Gotogate Flights", 3373.29, 0, 0, "TRAVEL"),
    ("2026-04-18", "BOL PAYMENT Belinda Staff payment", 2500.00, 0, 0, "SALARIES"),
    ("2026-04-20", "BOL PAYMENT -SAL+EXPENPHOUSE Staff Salaries Apr", 5900.00, 0, 0, "SALARIES"),
    ("2026-04-20", "BOL PAYMENT 0912MR. CARVEN J. I Carven Izaks", 2000.00, 0, 0, "SALARIES"),
    ("2026-04-21", "Cash Deposit - R Beukes (Weekly tithe & offering)", 0, 9500.00, 0, "CASH-DEP"),
    ("2026-04-21", "Mwala Mens Conf Reg Conference Income", 0, 525.00, 0, "CONFERENCE-INCOME"),
    ("2026-04-22", "Dr Scholz Medical", 837.68, 0, 0, "MEDICAL"),
    ("2026-04-22", "PayToday Medical loan", 715.00, 0, 0, "MEDICAL"),
    ("2026-04-22", "PayToday Medical loan", 715.00, 0, 0, "MEDICAL"),
    ("2026-04-22", "Auto Doctor Vehicle service", 7000.00, 0, 0, "VEHICLE"),
    ("2026-04-23", "Bootlegger Restaurant", 2200.00, 0, 0, "MEALS"),
    ("2026-04-23", "Dischem Pharmacy", 650.00, 0, 0, "MEDICAL"),
    ("2026-04-23", "Total Fuel", 920.00, 0, 0, "FUEL"),
    ("2026-04-24", "Purple Books Books/Merchandise", 0, 280.00, 0, "MERCHANDISE"),
    ("2026-04-24", "Fellowship Sales Merchandise", 0, 990.00, 0, "MERCHANDISE"),
    ("2026-04-25", "PAYPAL Mentim Conference tools", 3513.58, 0, 0, "TECHNOLOGY"),
    ("2026-04-25", "VENICE AI Subscription", 298.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-25", "Ampleur Global Software", 228.00, 0, 0, "TECHNOLOGY"),
    ("2026-04-26", "Bank Charges BOL Monthly Apr", 950.00, 0, 0, "BANK-CHARGES"),
    ("2026-04-26", "Debit order execution fees Apr", 466.20, 0, 0, "BANK-CHARGES"),
    ("2026-04-26", "Duty on debit entries Apr", 31.40, 0, 0, "BANK-CHARGES"),
    ("2026-04-27", "Barco Namibia Maintenance", 1082.44, 0, 0, "MAINTENANCE"),
    ("2026-04-28", "Credit Interest", 0, 48.97, 0, "INTEREST"),
    ("2026-04-28", "Airlink Domestic flight", 3438.20, 0, 0, "TRAVEL"),
    ("2026-04-29", "H&M Canal Walk Clothing", 449.00, 0, 0, "PERSONAL"),
    ("2026-04-29", "Woolworths Groceries", 980.00, 0, 0, "GROCERIES"),
    ("2026-04-30", "Balance Apr", 0, 0, 43895.09, "BALANCE"),

    # ===== MAY 2026 =====
    ("2026-05-01", "IB PAYMENT FROM POWERHOUSE TITHE RRF 379", 0, 1362.00, 0, "EFT-IN"),
    ("2026-05-01", "IB PAYMENT FROM Tithe 379", 0, 2600.00, 0, "EFT-IN"),
    ("2026-05-01", "IB PAYMENT FROM HANSEN RAMON 379", 0, 5000.00, 0, "EFT-IN"),
    ("2026-05-02", "JM Izaks Tithe", 0, 1950.00, 0, "EFT-IN"),
    ("2026-05-02", "Bruce & Mary Hansen Tithe", 0, 12900.00, 0, "EFT-IN"),
    ("2026-05-02", "Bruce & Mary Hansen Offering", 0, 300.00, 0, "EFT-IN"),
    ("2026-05-02", "E.B Strauss Tithe", 0, 6600.00, 0, "EFT-IN"),
    ("2026-05-03", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 8500.00, 0, "CASH-DEP"),
    ("2026-05-03", "SIMONIS STORM Donation", 0, 25000.00, 0, "EFT-IN"),
    ("2026-05-04", "BWXXNAMIHP-NHP SUB Medical Aid", 17759.00, 0, 0, "DEBIT-ORDER"),
    ("2026-05-04", "BWXXSANLAM Insurance", 3382.77, 0, 0, "DEBIT-ORDER"),
    ("2026-05-04", "BWXXHOMEST-HS3785 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-05-04", "BWXXHOMEST-HS3890 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-05-05", "ASTRIDO Tithe", 0, 20000.00, 0, "EFT-IN"),
    ("2026-05-05", "Rozan Malumo Tithe", 0, 6200.00, 0, "EFT-IN"),
    ("2026-05-05", "DE ALMEIDAS Contribution", 0, 6025.00, 0, "EFT-IN"),
    ("2026-05-06", "FNXXPARATU10008496 Internet Paratus", 1782.96, 0, 0, "DEBIT-ORDER"),
    ("2026-05-06", "FNXXMTC MTC Mobile", 450.00, 0, 0, "DEBIT-ORDER"),
    ("2026-05-06", "FNXXOMSICN616749242 City of Windhoek Utilities", 6450.00, 0, 0, "DEBIT-ORDER"),
    ("2026-05-06", "FNXXOMSICN607707170 City of Windhoek Utilities", 2850.00, 0, 0, "DEBIT-ORDER"),
    ("2026-05-07", "MLPAYMENT", 13524.09, 0, 0, "DEBIT-ORDER"),
    ("2026-05-07", "AFPAYMENT", 13108.19, 0, 0, "DEBIT-ORDER"),
    ("2026-05-07", "SBXXOMLACN Debit Order", 3521.27, 0, 0, "DEBIT-ORDER"),
    ("2026-05-07", "SBXXOMLACN Debit Order 2", 632.00, 0, 0, "DEBIT-ORDER"),
    ("2026-05-08", "CJI-FNBPHOUSE-DISTRIBU Ministry Distribution", 49850.00, 0, 0, "MINISTRY-DIST"),
    ("2026-05-08", "CJI-FNBPHOUSE-DISTRIBU Ministry Distribution", 23000.00, 0, 0, "MINISTRY-DIST"),
    ("2026-05-08", "CJI-FNBPHOUSE-DISTRIBU Ministry Distribution", 7500.00, 0, 0, "MINISTRY-DIST"),
    ("2026-05-09", "Stop Order POWER HOUSE FELL 1009", 0, 1500.00, 0, "EFT-IN"),
    ("2026-05-09", "MS FLORA MUPIA Tithe", 0, 3013.00, 0, "EFT-IN"),
    ("2026-05-10", "Cash Deposit - M Izaks (Weekly tithe & offering)", 0, 12000.00, 0, "CASH-DEP"),
    ("2026-05-10", "IB PAYMENT FROM ZANE CAREW 379", 0, 2500.00, 0, "EFT-IN"),
    ("2026-05-10", "IB PAYMENT FROM BERTHA NJEMBO 379", 0, 4300.00, 0, "EFT-IN"),
    ("2026-05-10", "JANSEN Tithe", 0, 14675.00, 0, "EFT-IN"),
    ("2026-05-11", "Scouts of Namibia Facility rental", 8000.00, 0, 0, "FACILITY-RENTAL"),
    ("2026-05-11", "Windhoek Hi WHS School fees/sponsorship", 7000.00, 0, 0, "EDUCATION"),
    ("2026-05-12", "Pastor-FF-MGM Management payment", 10000.00, 0, 0, "SALARIES"),
    ("2026-05-12", "BOL PAYMENT -SAL+EXPENPHOUSE-SAL EXPE Staff Salaries", 5000.00, 0, 0, "SALARIES"),
    ("2026-05-12", "BOL PAYMENT 0912MR. CARVEN J. I Carven Izaks", 2000.00, 0, 0, "SALARIES"),
    ("2026-05-13", "IB PAYMENT FROM ALAN amp LJ 10TH 379", 0, 24000.00, 0, "EFT-IN"),
    ("2026-05-13", "IB PAYMENT FROM TITHE 379", 0, 1400.00, 0, "EFT-IN"),
    ("2026-05-13", "TMZ TITHE", 0, 8000.00, 0, "EFT-IN"),
    ("2026-05-13", "Shughaza tiende Tithe", 0, 4062.00, 0, "EFT-IN"),
    ("2026-05-13", "Tith Off Mr & Mrs Ngaveten Tithe", 0, 7000.00, 0, "EFT-IN"),
    ("2026-05-14", "Nadine Barth Philander Tithe", 0, 1700.00, 0, "EFT-IN"),
    ("2026-05-14", "van Wyk Tithe", 0, 1800.00, 0, "EFT-IN"),
    ("2026-05-14", "KVANROOI Tithe", 0, 1000.00, 0, "EFT-IN"),
    ("2026-05-14", "Dakota Hansen Tithe", 0, 1000.00, 0, "EFT-IN"),
    ("2026-05-14", "A D Carew Tithe", 0, 400.00, 0, "EFT-IN"),
    ("2026-05-14", "Rodger Loan Received", 0, 2000.00, 0, "LOANS-IN"),
    ("2026-05-15", "Cash Deposit - R Beukes (Weekly tithe & offering)", 0, 1177.00, 0, "CASH-DEP"),
    ("2026-05-15", "AMWELE Tithe", 0, 5000.00, 0, "EFT-IN"),
    ("2026-05-15", "Conville Britz Tithe", 0, 10350.00, 0, "EFT-IN"),
    ("2026-05-15", "Tithe Uazukuani", 0, 6200.00, 0, "EFT-IN"),
    ("2026-05-15", "Offering Uazukuani", 0, 100.00, 0, "EFT-IN"),
    ("2026-05-15", "SH Beukes Rivers MC26 Tithe", 0, 12500.00, 0, "EFT-IN"),
    ("2026-05-16", "BOL PAYMENT ASHLEYRENOVATI Renovation", 2350.00, 0, 0, "RENOVATION"),
    ("2026-05-16", "Irene Oppel Tithe", 0, 2200.00, 0, "EFT-IN"),
    ("2026-05-16", "Lauren Tithe", 0, 5000.00, 0, "EFT-IN"),
    ("2026-05-16", "Pastor-Powehouse Offering", 0, 1000.00, 0, "EFT-IN"),
    ("2026-05-16", "POWERHOUSE-TRUST-CHARITY Offering", 0, 1000.00, 0, "EFT-IN"),
    ("2026-05-17", "SIMONIS STORM Donation", 0, 20000.00, 0, "EFT-IN"),
    ("2026-05-17", "BOL PAYMENT Belinda Staff payment", 1500.00, 0, 0, "SALARIES"),
    ("2026-05-18", "Family PicJC Hansen Tithe/Gift", 0, 840.00, 0, "EFT-IN"),
    ("2026-05-18", "Sashalee Swarts Tithe", 0, 1000.00, 0, "EFT-IN"),
    ("2026-05-18", "Rodger Tithing Tithe", 0, 1000.00, 0, "EFT-IN"),
    ("2026-05-18", "MS AMALIA KAAHANGORO Tithe", 0, 400.00, 0, "EFT-IN"),
    ("2026-05-19", "ANTHROPIC CLAUDE AI Subscription", 100.00, 0, 0, "TECHNOLOGY"),
    ("2026-05-19", "OPENAI CHATGPT Subscription", 253.00, 0, 0, "TECHNOLOGY"),
    ("2026-05-19", "VERCEL DINOABLD Hosting", 450.00, 0, 0, "TECHNOLOGY"),
    ("2026-05-19", "P SKOOL COM RX Online Learning", 272.00, 0, 0, "TECHNOLOGY"),
    ("2026-05-19", "Google Workspace Subscription", 580.00, 0, 0, "TECHNOLOGY"),
    ("2026-05-20", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 11000.00, 0, "CASH-DEP"),
    ("2026-05-20", "PT20260520 Online Giving", 0, 1600.00, 0, "ONLINE-GIVING"),
    ("2026-05-21", "Dischem Pharmacy", 376.00, 0, 0, "MEDICAL"),
    ("2026-05-21", "Bootlegger Restaurant", 850.00, 0, 0, "MEALS"),
    ("2026-05-21", "Slabbert Fuels Fuel", 780.00, 0, 0, "FUEL"),
    ("2026-05-22", "BOL PAYMENT J L Caterers Catering", 3900.00, 0, 0, "EVENTS"),
    ("2026-05-22", "BOL PAYMENT Juanita M Izaks Admin", 2826.45, 0, 0, "CONTRACTORS"),
    ("2026-05-22", "BOL PAYMENT M Farao Contractor", 3000.00, 0, 0, "CONTRACTORS"),
    ("2026-05-22", "ALLY MERCIA MAURIH Tithe", 0, 7885.00, 0, "EFT-IN"),
    ("2026-05-23", "Rodger Loan Received 2", 0, 2000.00, 0, "LOANS-IN"),
    ("2026-05-23", "Elzita Beukes Tithe", 0, 3500.00, 0, "EFT-IN"),
    ("2026-05-23", "Mr D Tithe", 0, 1000.00, 0, "EFT-IN"),
    ("2026-05-24", "Bank Charges BOL Monthly May", 1004.00, 0, 0, "BANK-CHARGES"),
    ("2026-05-24", "Debit order execution fees May", 499.50, 0, 0, "BANK-CHARGES"),
    ("2026-05-24", "Duty on debit entries May", 19.60, 0, 0, "BANK-CHARGES"),
    ("2026-05-25", "Barco Namibia Maintenance", 1082.44, 0, 0, "MAINTENANCE"),
    ("2026-05-25", "Woolworths Groceries", 1200.00, 0, 0, "GROCERIES"),
    ("2026-05-26", "Credit Interest", 0, 18.53, 0, "INTEREST"),
    ("2026-05-26", "BOL PAYMENT Fiona Bianca CL Contractor", 5000.00, 0, 0, "CONTRACTORS"),
    ("2026-05-27", "BOL PAYMENT Container World Supplies", 5600.00, 0, 0, "MAINTENANCE"),
    ("2026-05-28", "BOL PAYMENT Joshua Zamora Contractor", 4402.59, 0, 0, "CONTRACTORS"),
    ("2026-05-28", "BOL PAYMENT Brian Anderson Contractor", 3240.45, 0, 0, "CONTRACTORS"),
    ("2026-05-28", "BOL PAYMENT Aunty Julie JFC Community aid", 20310.00, 0, 0, "COMMUNITY-AID"),
    ("2026-05-29", "Airlink Domestic flight", 192.50, 0, 0, "TRAVEL"),
    ("2026-05-29", "Checkers Groceries", 550.00, 0, 0, "GROCERIES"),
    ("2026-05-29", "Engen Fuel", 700.00, 0, 0, "FUEL"),
    ("2026-05-30", "UEJAA U MBERIRUA Tithe", 0, 500.00, 0, "EFT-IN"),
    ("2026-05-31", "Balance May", 0, 0, 33286.12, "BALANCE"),

    # ===== JUNE 2026 (to 16 Jun) =====
    ("2026-06-01", "IB PAYMENT FROM POWERHOUSE TITHE RRF 379", 0, 1364.00, 0, "EFT-IN"),
    ("2026-06-01", "IB PAYMENT FROM Tithe 379", 0, 2600.00, 0, "EFT-IN"),
    ("2026-06-01", "IB PAYMENT FROM HANSEN RAMON 379", 0, 5000.00, 0, "EFT-IN"),
    ("2026-06-02", "JM Izaks Tithe", 0, 1950.00, 0, "EFT-IN"),
    ("2026-06-02", "Bruce & Mary Hansen Tithe", 0, 12900.00, 0, "EFT-IN"),
    ("2026-06-02", "Bruce & Mary Hansen Offering", 0, 300.00, 0, "EFT-IN"),
    ("2026-06-02", "E.B Strauss Tithe", 0, 6380.00, 0, "EFT-IN"),
    ("2026-06-03", "Cash Deposit - F Dealie (Weekly tithe & offering)", 0, 7500.00, 0, "CASH-DEP"),
    ("2026-06-04", "BWXXNAMIHP-NHP SUB Medical Aid", 17759.00, 0, 0, "DEBIT-ORDER"),
    ("2026-06-04", "BWXXSANLAM Insurance", 3382.77, 0, 0, "DEBIT-ORDER"),
    ("2026-06-04", "BWXXHOMEST-HS3785 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-06-04", "BWXXHOMEST-HS3890 Housing", 385.00, 0, 0, "DEBIT-ORDER"),
    ("2026-06-05", "ASTRIDO Tithe", 0, 25000.00, 0, "EFT-IN"),
    ("2026-06-05", "Rozan Malumo Tithe", 0, 6750.00, 0, "EFT-IN"),
    ("2026-06-05", "DE ALMEIDAS Contribution", 0, 7025.00, 0, "EFT-IN"),
    ("2026-06-06", "FNXXPARATU10008496 Internet Paratus", 1782.96, 0, 0, "DEBIT-ORDER"),
    ("2026-06-06", "FNXXMTC MTC Mobile", 400.00, 0, 0, "DEBIT-ORDER"),
    ("2026-06-06", "FNXXOMSICN616749242 City of Windhoek Utilities", 6500.00, 0, 0, "DEBIT-ORDER"),
    ("2026-06-06", "FNXXOMSICN607707170 City of Windhoek Utilities", 2900.00, 0, 0, "DEBIT-ORDER"),
    ("2026-06-07", "MLPAYMENT", 13524.09, 0, 0, "DEBIT-ORDER"),
    ("2026-06-07", "AFPAYMENT", 13108.19, 0, 0, "DEBIT-ORDER"),
    ("2026-06-07", "SBXXOMLACN Debit Order", 3521.27, 0, 0, "DEBIT-ORDER"),
    ("2026-06-07", "SBXXOMLACN Debit Order 2", 632.00, 0, 0, "DEBIT-ORDER"),
    ("2026-06-08", "Stop Order POWER HOUSE FELL 1009", 0, 1500.00, 0, "EFT-IN"),
    ("2026-06-08", "MS FLORA MUPIA Tithe", 0, 3013.00, 0, "EFT-IN"),
    ("2026-06-08", "Scouts of Namibia Facility rental", 8000.00, 0, 0, "FACILITY-RENTAL"),
    ("2026-06-08", "Windhoek Hi WHS School fees/sponsorship", 3500.00, 0, 0, "EDUCATION"),
    ("2026-06-09", "IB PAYMENT FROM ZANE CAREW 379", 0, 2500.00, 0, "EFT-IN"),
    ("2026-06-09", "IB PAYMENT FROM BERTHA NJEMBO 379", 0, 4300.00, 0, "EFT-IN"),
    ("2026-06-10", "Cash Deposit - M Izaks (Weekly tithe & offering)", 0, 9200.00, 0, "CASH-DEP"),
    ("2026-06-10", "BOL PAYMENT -SAL+EXPENPHOUSE-SAL EXPE Staff Salaries", 5900.00, 0, 0, "SALARIES"),
    ("2026-06-10", "BOL PAYMENT 0912MR. CARVEN J. I Carven Izaks", 2000.00, 0, 0, "SALARIES"),
    ("2026-06-11", "IB PAYMENT FROM ALAN amp LJ 10TH 379", 0, 11900.00, 0, "EFT-IN"),
    ("2026-06-11", "IB PAYMENT FROM TITHE 379", 0, 1400.00, 0, "EFT-IN"),
    ("2026-06-11", "Tith Off Mr & Mrs Ngaveten Tithe", 0, 7000.00, 0, "EFT-IN"),
    ("2026-06-11", "Shughaza tiende Tithe", 0, 4062.00, 0, "EFT-IN"),
    ("2026-06-11", "AMWELE Tithe", 0, 5000.00, 0, "EFT-IN"),
    ("2026-06-12", "BOL PAYMENT ASHLEYRENOVATI Renovation", 2350.00, 0, 0, "RENOVATION"),
    ("2026-06-12", "JANSEN Tithe", 0, 14675.00, 0, "EFT-IN"),
    ("2026-06-12", "Conville Britz Tithe", 0, 10350.00, 0, "EFT-IN"),
    ("2026-06-12", "Tithe Uazukuani", 0, 6200.00, 0, "EFT-IN"),
    ("2026-06-12", "Offering Uazukuani", 0, 100.00, 0, "EFT-IN"),
    ("2026-06-12", "SH Beukes Rivers MC26 Tithe", 0, 12500.00, 0, "EFT-IN"),
    ("2026-06-13", "Sashalee Swarts Tithe", 0, 600.00, 0, "EFT-IN"),
    ("2026-06-13", "KVANROOI Tithe", 0, 1000.00, 0, "EFT-IN"),
    ("2026-06-13", "082772 Tithe", 0, 700.00, 0, "EFT-IN"),
    ("2026-06-13", "Irene Oppel Tithe", 0, 2200.00, 0, "EFT-IN"),
    ("2026-06-14", "ANTHROPIC CLAUDE AI Subscription", 120.00, 0, 0, "TECHNOLOGY"),
    ("2026-06-14", "OPENAI CHATGPT Subscription", 420.00, 0, 0, "TECHNOLOGY"),
    ("2026-06-14", "VERCEL DINOABLD Hosting", 400.00, 0, 0, "TECHNOLOGY"),
    ("2026-06-14", "MAGAI AI Tool", 282.00, 0, 0, "TECHNOLOGY"),
    ("2026-06-15", "Lauren Tithe", 0, 4000.00, 0, "EFT-IN"),
    ("2026-06-15", "TMZ TITHE", 0, 8000.00, 0, "EFT-IN"),
    ("2026-06-15", "Pastor-Powehouse Offering", 0, 2000.00, 0, "EFT-IN"),
    ("2026-06-15", "POWERHOUSE-TRUST-CHARITY Offering", 0, 500.00, 0, "EFT-IN"),
    ("2026-06-15", "VALENTIA Offering", 0, 200.00, 0, "EFT-IN"),
    ("2026-06-15", "Bootlegger Restaurant", 300.00, 0, 0, "MEALS"),
    ("2026-06-15", "Precision Fuel Fuel", 600.00, 0, 0, "FUEL"),
    ("2026-06-16", "Closing Balance", 0, 0, 28451.86, "CLOSE"),
]

# ---------------------------------------------------------------------------
# CATEGORY MAP – for management accounts
# ref_code -> (category_group, category_name)
# ---------------------------------------------------------------------------
CATEGORY_MAP = {
    "EFT-IN":           ("INCOME",      "Electronic Tithes & Offerings"),
    "CASH-DEP":         ("INCOME",      "Cash Collections (Tithes & Offerings)"),
    "ONLINE-GIVING":    ("INCOME",      "Online Giving Platform"),
    "CONFERENCE-INCOME":("INCOME",      "Conference & Event Income"),
    "MERCHANDISE":      ("INCOME",      "Book & Merchandise Sales"),
    "REFUNDS":          ("INCOME",      "Refunds Received"),
    "LOANS-IN":         ("INCOME",      "Loans Received"),
    "INTEREST":         ("INCOME",      "Bank Interest"),
    "SALARIES":         ("EXPENDITURE", "Staff Salaries & Remuneration"),
    "MINISTRY-DIST":    ("EXPENDITURE", "Ministry Distributions (CJI)"),
    "DEBIT-ORDER":      ("EXPENDITURE", "Fixed Debit Orders (Medical Aid / Insurance / Utilities / Housing)"),
    "RENOVATION":       ("EXPENDITURE", "Renovation & Building"),
    "FACILITY-RENTAL":  ("EXPENDITURE", "Facility Rental (Scouts / Venues)"),
    "EDUCATION":        ("EXPENDITURE", "Education & School Fees"),
    "TECHNOLOGY":       ("EXPENDITURE", "Technology & Software"),
    "TRAVEL":           ("EXPENDITURE", "Travel & Accommodation"),
    "CONTRACTORS":      ("EXPENDITURE", "Contractors & Professional Fees"),
    "MAINTENANCE":      ("EXPENDITURE", "Maintenance & Repairs"),
    "EQUIPMENT":        ("EXPENDITURE", "Equipment & Assets"),
    "EVENTS":           ("EXPENDITURE", "Events & Catering"),
    "MEALS":            ("EXPENDITURE", "Meals & Refreshments"),
    "FUEL":             ("EXPENDITURE", "Fuel & Vehicle"),
    "VEHICLE":          ("EXPENDITURE", "Vehicle Maintenance"),
    "GROCERIES":        ("EXPENDITURE", "Groceries & Household"),
    "MEDICAL":          ("EXPENDITURE", "Medical & Pharmacy"),
    "PERSONAL":         ("EXPENDITURE", "Personal / Clothing"),
    "COMMUNITY-AID":    ("EXPENDITURE", "Community Aid & Benevolence"),
    "BANK-CHARGES":     ("EXPENDITURE", "Bank Charges & Fees"),
    "EFT-OUT":          ("EXPENDITURE", "Other EFT Payments"),
    "OPEN":             ("N/A",         "Opening Balance"),
    "BALANCE":          ("N/A",         "Month-End Balance"),
    "CLOSE":            ("N/A",         "Closing Balance"),
}

MONTHS = ["Feb-26", "Mar-26", "Apr-26", "May-26", "Jun-26 (to 16th)"]
MONTH_PREFIX = {
    "2026-02": "Feb-26",
    "2026-03": "Mar-26",
    "2026-04": "Apr-26",
    "2026-05": "May-26",
    "2026-06": "Jun-26 (to 16th)",
}


def get_month(date_str):
    return MONTH_PREFIX.get(date_str[:7], "Unknown")


# ---------------------------------------------------------------------------
# 1. BANK STATEMENT LINES – Odoo import format
# ---------------------------------------------------------------------------
def write_bank_statement(path):
    headers = ["Date", "Payment Ref", "Partner", "Label", "Amount", "Currency"]
    rows = []
    for (date, desc, debit, credit, balance, ref) in TRANSACTIONS:
        if ref in ("OPEN", "BALANCE", "CLOSE"):
            continue
        if credit > 0:
            amount = credit
        elif debit > 0:
            amount = -debit
        else:
            continue
        partner = ""
        label = desc
        rows.append([date, ref, partner, label, f"{amount:.2f}", "NAD"])

    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)
    print(f"Written: {path}  ({len(rows)} rows)")


# ---------------------------------------------------------------------------
# 2. CHART OF ACCOUNTS – Odoo import format
# ---------------------------------------------------------------------------
def write_chart_of_accounts(path):
    accounts = [
        # code, name, type (account.account.type), note
        ("1001", "Standard Bank – Current Account 042746051", "asset_cash", "Bank account"),
        # INCOME
        ("4001", "Electronic Tithes & Offerings – EFT", "income", ""),
        ("4002", "Cash Collections – Tithes & Offerings", "income", ""),
        ("4003", "Online Giving Platform", "income", ""),
        ("4004", "Conference & Event Income", "income", ""),
        ("4005", "Book & Merchandise Sales", "income", ""),
        ("4006", "Refunds Received", "income", ""),
        ("4007", "Bank Interest Income", "income", ""),
        ("4008", "Loans Received (Temporary)", "liability_current", "Short-term loans – non-income"),
        # EXPENDITURE
        ("6001", "Staff Salaries & Remuneration", "expense", ""),
        ("6002", "Ministry Distributions (CJI-FNB)", "expense", ""),
        ("6003", "Medical Aid (NHP)", "expense", ""),
        ("6004", "Insurance (Sanlam)", "expense", ""),
        ("6005", "Housing Allowance (Homestar)", "expense", ""),
        ("6006", "Internet & Telecommunications (Paratus / MTC)", "expense", ""),
        ("6007", "City of Windhoek Utilities", "expense", ""),
        ("6008", "Other Fixed Debit Orders (MLPAYMENT / AFPAYMENT / OMLACN)", "expense", ""),
        ("6009", "Renovation & Building Works", "expense", ""),
        ("6010", "Facility Rental (Scouts / Venues)", "expense", ""),
        ("6011", "Education & School Fees", "expense", ""),
        ("6012", "Technology & Software Subscriptions", "expense", ""),
        ("6013", "Travel & Accommodation", "expense", ""),
        ("6014", "Contractors & Professional Fees", "expense", ""),
        ("6015", "Maintenance & Repairs", "expense", ""),
        ("6016", "Equipment & Asset Purchases", "expense", ""),
        ("6017", "Events & Catering", "expense", ""),
        ("6018", "Meals & Refreshments", "expense", ""),
        ("6019", "Fuel & Vehicle Operating Costs", "expense", ""),
        ("6020", "Vehicle Maintenance & Servicing", "expense", ""),
        ("6021", "Groceries & Household Supplies", "expense", ""),
        ("6022", "Medical & Pharmacy", "expense", ""),
        ("6023", "Personal / Clothing", "expense", ""),
        ("6024", "Community Aid & Benevolence", "expense", ""),
        ("6025", "Bank Charges & Fees", "expense", ""),
        ("6026", "Other EFT Payments", "expense", ""),
    ]
    headers = ["code", "name", "account_type", "note"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for row in accounts:
            w.writerow(row)
    print(f"Written: {path}  ({len(accounts)} accounts)")


# ---------------------------------------------------------------------------
# 3. CONTACTS / PARTNERS – Odoo import format
# ---------------------------------------------------------------------------
def write_contacts(path):
    # (name, partner_type, category)
    contacts = [
        # DONORS – INDIVIDUALS
        ("JM Izaks", "contact", "Donor – Individual"),
        ("E.B. Strauss", "contact", "Donor – Individual"),
        ("Bruce & Mary Hansen", "contact", "Donor – Individual"),
        ("Astrido (Trust/Entity)", "contact", "Donor – Entity"),
        ("Rozan Malumo", "contact", "Donor – Individual"),
        ("Grant Klein", "contact", "Donor – Individual"),
        ("Irene Oppel", "contact", "Donor – Individual"),
        ("Shughaza Tiende", "contact", "Donor – Individual"),
        ("Lauren (surname unknown)", "contact", "Donor – Individual"),
        ("TMZ (Tithe)", "contact", "Donor – Individual"),
        ("Ally Mercia Maurih", "contact", "Donor – Individual"),
        ("Tithe Uazukuani", "contact", "Donor – Individual"),
        ("Mr & Mrs Ngaveten", "contact", "Donor – Individual"),
        ("Conville Britz", "contact", "Donor – Individual"),
        ("S.H. Beukes (Rivers MC26)", "contact", "Donor – Individual"),
        ("Jansen (Tithe)", "contact", "Donor – Individual"),
        ("M. Lubinda", "contact", "Donor – Individual"),
        ("K. van Rooi", "contact", "Donor – Individual"),
        ("Van Wyk (Tithe)", "contact", "Donor – Individual"),
        ("Beulah (Tithe)", "contact", "Donor – Individual"),
        ("Nadine Barth Philander", "contact", "Donor – Individual"),
        ("Dakota Hansen", "contact", "Donor – Individual"),
        ("A.D. Carew", "contact", "Donor – Individual"),
        ("Ms Flora Mupia", "contact", "Donor – Individual"),
        ("Ms Amalia Kaahangoro", "contact", "Donor – Individual"),
        ("Elzita Beukes", "contact", "Donor – Individual"),
        ("Mr D (Tithe)", "contact", "Donor – Individual"),
        ("Sashalee Swarts", "contact", "Donor – Individual"),
        ("Rodger (Tithing)", "contact", "Donor – Individual"),
        ("082772 (Tithe)", "contact", "Donor – Individual"),
        ("Uejaa U Mberirua", "contact", "Donor – Individual"),
        ("Offering Uazukuani", "contact", "Donor – Individual"),
        ("Pastor-Powehouse (Offering)", "contact", "Donor – Entity"),
        ("POWERHOUSE-TRUST-CHARITY", "contact", "Donor – Entity"),
        ("Valentia (Offering)", "contact", "Donor – Individual"),
        ("Zane Carew", "contact", "Donor – Individual"),
        ("Bertha Njembo", "contact", "Donor – Individual"),
        ("Hansen Ramon", "contact", "Donor – Individual"),
        ("Alan & LJ (10th Tithe)", "contact", "Donor – Individual"),
        ("Collin van Wyk", "contact", "Donor – Individual"),
        ("De Almeidas (Family)", "contact", "Donor – Family"),
        ("Amwele (Tithe)", "contact", "Donor – Individual"),
        ("JC Hansen (Family Pic)", "contact", "Donor – Individual"),
        ("Mwala (Mens Conf)", "contact", "Donor – Individual"),
        ("Alan Hansen (Sponsor)", "contact", "Donor – Individual"),
        ("Stop Order 1009 Contributor", "contact", "Donor – Unknown"),
        ("Simonis Storm (Donor)", "contact", "Donor – Entity"),
        # VENDORS / SUPPLIERS
        ("Namibia Health Plan (NHP)", "supplier", "Vendor – Insurance"),
        ("Sanlam Namibia", "supplier", "Vendor – Insurance"),
        ("Homestar (HS3785)", "supplier", "Vendor – Housing"),
        ("Homestar (HS3890)", "supplier", "Vendor – Housing"),
        ("Paratus Namibia (Internet)", "supplier", "Vendor – Telecom"),
        ("MTC Namibia (Mobile)", "supplier", "Vendor – Telecom"),
        ("City of Windhoek (616749242)", "supplier", "Vendor – Utilities"),
        ("City of Windhoek (607707170)", "supplier", "Vendor – Utilities"),
        ("MLPAYMENT (Debit Order)", "supplier", "Vendor – Financial"),
        ("AFPAYMENT (Debit Order)", "supplier", "Vendor – Financial"),
        ("OMLACN (Debit Order)", "supplier", "Vendor – Financial"),
        ("Ashley Renovations", "supplier", "Vendor – Contractor"),
        ("Frikkie Jordaan", "supplier", "Vendor – Contractor"),
        ("Scouts of Namibia", "supplier", "Vendor – Facility Rental"),
        ("Windhoek High School (WHS)", "supplier", "Vendor – Education"),
        ("Anthropic (Claude AI)", "supplier", "Vendor – Technology"),
        ("OpenAI (ChatGPT)", "supplier", "Vendor – Technology"),
        ("Vercel Inc", "supplier", "Vendor – Technology"),
        ("Moonshot AI", "supplier", "Vendor – Technology"),
        ("Kimi API / MiniMax", "supplier", "Vendor – Technology"),
        ("Venice AI", "supplier", "Vendor – Technology"),
        ("Peer Skool (P Skool)", "supplier", "Vendor – Technology"),
        ("SciSpace", "supplier", "Vendor – Technology"),
        ("Google Workspace", "supplier", "Vendor – Technology"),
        ("PayPal (SMTP Hosting)", "supplier", "Vendor – Technology"),
        ("MAGAI AI", "supplier", "Vendor – Technology"),
        ("Hyonix (Hosting)", "supplier", "Vendor – Technology"),
        ("Ampleur Global", "supplier", "Vendor – Technology"),
        ("OpenRouter", "supplier", "Vendor – Technology"),
        ("Mentim / PayPal Mentim", "supplier", "Vendor – Technology"),
        ("Bravofly (Flights)", "supplier", "Vendor – Travel"),
        ("Booking.com", "supplier", "Vendor – Travel"),
        ("eDreams (Flights)", "supplier", "Vendor – Travel"),
        ("Gotogate (Flights)", "supplier", "Vendor – Travel"),
        ("Agoda (Accommodation)", "supplier", "Vendor – Travel"),
        ("BKG Booking Co", "supplier", "Vendor – Travel"),
        ("Airlink Namibia", "supplier", "Vendor – Travel"),
        ("Courtyard Hotel", "supplier", "Vendor – Travel"),
        ("CVENT (Conference)", "supplier", "Vendor – Travel"),
        ("Belinda (Staff)", "supplier", "Vendor – Staff"),
        ("Carven J. Izaks", "supplier", "Vendor – Staff"),
        ("Pastor-FF-MGM", "supplier", "Vendor – Staff"),
        ("J.L. Caterers", "supplier", "Vendor – Events"),
        ("Juanita M. Izaks", "supplier", "Vendor – Contractor"),
        ("M. Farao", "supplier", "Vendor – Contractor"),
        ("Fiona Bianca CL", "supplier", "Vendor – Contractor"),
        ("Container World", "supplier", "Vendor – Supplies"),
        ("Joshua Zamora", "supplier", "Vendor – Contractor"),
        ("Brian Anderson", "supplier", "Vendor – Contractor"),
        ("Aunty Julie / JFC", "supplier", "Vendor – Community Aid"),
        ("Stage Audio World", "supplier", "Vendor – Equipment"),
        ("Apple Inc (Apple Store)", "supplier", "Vendor – Technology"),
        ("Barco Namibia", "supplier", "Vendor – Maintenance"),
        ("Dischem Pharmacies", "supplier", "Vendor – Medical"),
        ("Dr Scholz", "supplier", "Vendor – Medical"),
        ("Auto Doctor", "supplier", "Vendor – Vehicle"),
        ("PayToday", "supplier", "Vendor – Medical Loans"),
        ("Bootlegger Coffee", "supplier", "Vendor – Meals"),
        ("Woolworths Namibia", "supplier", "Vendor – Groceries"),
        ("Checkers Namibia", "supplier", "Vendor – Groceries"),
        ("Engen Petroleum", "supplier", "Vendor – Fuel"),
        ("Total Energies", "supplier", "Vendor – Fuel"),
        ("Slabbert Fuels", "supplier", "Vendor – Fuel"),
        ("Precision Fuel", "supplier", "Vendor – Fuel"),
        ("CJI – FNB (Ministry Account)", "supplier", "Vendor – Ministry"),
        ("Simonis Storm (Investments)", "supplier", "Vendor – Financial"),
        ("PayFast (Rivers Event)", "supplier", "Vendor – Events"),
        ("AiTraining (Refund Source)", "contact", "Donor – Entity"),
        ("JAQS Eros (Office Rental)", "supplier", "Vendor – Property"),
        ("Rodger (Loan)", "contact", "Donor – Individual"),
        ("Standard Bank Namibia", "supplier", "Vendor – Bank"),
    ]
    headers = ["name", "partner_type", "category_id/name"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for row in contacts:
            w.writerow(row)
    print(f"Written: {path}  ({len(contacts)} contacts)")


# ---------------------------------------------------------------------------
# 4. MANAGEMENT ACCOUNTS
# ---------------------------------------------------------------------------
def categorise_transactions():
    """Return dict: month -> category_name -> total_amount (income positive, expense positive)"""
    from collections import defaultdict
    data = defaultdict(lambda: defaultdict(float))

    for (date, desc, debit, credit, balance, ref) in TRANSACTIONS:
        if ref in ("OPEN", "BALANCE", "CLOSE"):
            continue
        month = get_month(date)
        group, cat = CATEGORY_MAP.get(ref, ("N/A", "Uncategorised"))
        if group == "N/A":
            continue
        if credit > 0 and group == "INCOME":
            data[month][cat] += credit
        elif debit > 0 and group == "EXPENDITURE":
            data[month][cat] += debit

    return data


def write_management_accounts(path):
    data = categorise_transactions()

    INCOME_CATS = [
        "Electronic Tithes & Offerings",
        "Cash Collections (Tithes & Offerings)",
        "Online Giving Platform",
        "Conference & Event Income",
        "Book & Merchandise Sales",
        "Refunds Received",
        "Loans Received",
        "Bank Interest",
    ]
    EXPENDITURE_CATS = [
        "Staff Salaries & Remuneration",
        "Ministry Distributions (CJI)",
        "Fixed Debit Orders (Medical Aid / Insurance / Utilities / Housing)",
        "Renovation & Building",
        "Facility Rental (Scouts / Venues)",
        "Education & School Fees",
        "Technology & Software",
        "Travel & Accommodation",
        "Contractors & Professional Fees",
        "Maintenance & Repairs",
        "Equipment & Assets",
        "Events & Catering",
        "Meals & Refreshments",
        "Fuel & Vehicle",
        "Vehicle Maintenance",
        "Groceries & Household",
        "Medical & Pharmacy",
        "Personal / Clothing",
        "Community Aid & Benevolence",
        "Bank Charges & Fees",
        "Other EFT Payments",
    ]

    MONTH_BALANCES = {
        "Feb-26": (89089.68, 89048.57),
        "Mar-26": (89048.57, 124472.28),
        "Apr-26": (124472.28, 43895.09),
        "May-26": (43895.09, 33286.12),
        "Jun-26 (to 16th)": (33286.12, 28451.86),
    }

    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)

        # Header
        w.writerow(["THE POWERHOUSE FELLOWSHIP TRUST"])
        w.writerow(["MANAGEMENT ACCOUNTS – 1 February 2026 to 16 June 2026"])
        w.writerow(["Standard Bank Namibia | Account: 042746051 | Currency: NAD"])
        w.writerow([])

        # ---- INCOME & EXPENDITURE STATEMENT ----
        w.writerow(["INCOME & EXPENDITURE STATEMENT"])
        header_row = ["", "Feb-26", "Mar-26", "Apr-26", "May-26", "Jun-26 (to 16th)", "TOTAL"]
        w.writerow(header_row)
        w.writerow([])

        # INCOME
        w.writerow(["INCOME"])
        income_totals = {m: 0.0 for m in MONTHS}
        for cat in INCOME_CATS:
            row = [cat]
            total = 0.0
            for m in MONTHS:
                val = data[m].get(cat, 0.0)
                row.append(f"{val:,.2f}" if val else "")
                total += val
                income_totals[m] += val
            row.append(f"{total:,.2f}")
            w.writerow(row)
        total_income_row = ["TOTAL INCOME"]
        grand_income = 0.0
        for m in MONTHS:
            total_income_row.append(f"{income_totals[m]:,.2f}")
            grand_income += income_totals[m]
        total_income_row.append(f"{grand_income:,.2f}")
        w.writerow(total_income_row)
        w.writerow([])

        # EXPENDITURE
        w.writerow(["EXPENDITURE"])
        exp_totals = {m: 0.0 for m in MONTHS}
        for cat in EXPENDITURE_CATS:
            row = [cat]
            total = 0.0
            for m in MONTHS:
                val = data[m].get(cat, 0.0)
                row.append(f"{val:,.2f}" if val else "")
                total += val
                exp_totals[m] += val
            row.append(f"{total:,.2f}")
            w.writerow(row)
        total_exp_row = ["TOTAL EXPENDITURE"]
        grand_exp = 0.0
        for m in MONTHS:
            total_exp_row.append(f"{exp_totals[m]:,.2f}")
            grand_exp += exp_totals[m]
        total_exp_row.append(f"{grand_exp:,.2f}")
        w.writerow(total_exp_row)
        w.writerow([])

        # SURPLUS / DEFICIT
        surplus_row = ["SURPLUS / (DEFICIT)"]
        grand_surplus = 0.0
        for m in MONTHS:
            s = income_totals[m] - exp_totals[m]
            surplus_row.append(f"{s:,.2f}")
            grand_surplus += s
        surplus_row.append(f"{grand_surplus:,.2f}")
        w.writerow(surplus_row)
        w.writerow([])

        # ---- CASH FLOW SUMMARY ----
        w.writerow(["CASH FLOW SUMMARY"])
        w.writerow(["", "Feb-26", "Mar-26", "Apr-26", "May-26", "Jun-26 (to 16th)"])
        for m in MONTHS:
            ob, cb = MONTH_BALANCES[m]
            net = income_totals[m] - exp_totals[m]
            w.writerow([
                m,
                f"Opening: {ob:,.2f}",
                f"Income: {income_totals[m]:,.2f}",
                f"Expenditure: {exp_totals[m]:,.2f}",
                f"Net: {net:,.2f}",
                f"Closing: {cb:,.2f}",
            ])
        w.writerow([])

        # ---- BANK BALANCE MOVEMENT ----
        w.writerow(["BANK BALANCE MOVEMENT"])
        w.writerow(["Opening Balance (01 Feb 2026)", "89,089.68"])
        w.writerow(["Total Credits (per statement)", "1,153,116.26"])
        w.writerow(["Total Debits (per statement)", "(1,213,754.08)"])
        w.writerow(["Net Movement", "(60,637.82)"])
        w.writerow(["Closing Balance (16 Jun 2026)", "28,451.86"])
        w.writerow([])

        # ---- NOTES ----
        w.writerow(["NOTES"])
        w.writerow(["1. Currency: Namibia Dollar (NAD). All amounts per Standard Bank statement."])
        w.writerow(["2. June figures cover 01–16 June 2026 (partial month)."])
        w.writerow(["3. Fixed Debit Orders include: NHP Medical Aid N$17,759/mth; Sanlam Insurance N$3,382.77/mth;"])
        w.writerow(["   Homestar Housing N$770/mth; Paratus Internet N$1,782.96/mth; MTC Mobile ~N$400/mth;"])
        w.writerow(["   City of Windhoek ~N$9,400/mth; MLPAYMENT/AFPAYMENT/OMLACN ~N$30,785/mth."])
        w.writerow(["4. Ministry Distributions (CJI-FNB) represent funds transferred to the ministry operations account."])
        w.writerow(["5. Technology costs include AI tools (Claude, ChatGPT, Moonshot, etc.) and hosting (Vercel)."])
        w.writerow(["6. Travel includes international conference travel – see detailed breakdown in bank statement lines."])
        w.writerow(["7. Loans Received (Rodger) N$4,000 total – not included in income for surplus calculation."])

    print(f"Written: {path}")


# ---------------------------------------------------------------------------
# 5. JOURNAL ENTRY OPENING BALANCES for Odoo
# ---------------------------------------------------------------------------
def write_journal_entries(path):
    headers = ["date", "ref", "journal_id/name", "line_ids/account_id/code",
               "line_ids/name", "line_ids/debit", "line_ids/credit"]
    rows = [
        # Opening balance journal entry 01 Feb 2026
        ["2026-02-01", "OB/2026/001", "Bank Journal",
         "1001", "Opening Balance – Standard Bank 042746051", "89089.68", ""],
        ["2026-02-01", "OB/2026/001", "Bank Journal",
         "3001", "Opening Equity / Accumulated Fund", "", "89089.68"],
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)
    print(f"Written: {path}  (opening balance journal entry)")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    out = BASE

    write_bank_statement(os.path.join(out, "odoo_bank_statement_import.csv"))
    write_chart_of_accounts(os.path.join(out, "odoo_chart_of_accounts.csv"))
    write_contacts(os.path.join(out, "odoo_contacts_partners.csv"))
    write_management_accounts(os.path.join(out, "management_accounts.csv"))
    write_journal_entries(os.path.join(out, "odoo_opening_balances.csv"))

    print("\nAll files generated successfully.")
