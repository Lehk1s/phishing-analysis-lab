# Phishing Analysis Lab

A hands-on cybersecurity project focused on email analysis, phishing indicators, and email security fundamentals using Python.

## About

Phishing Analysis Lab is a learning project designed to explore how suspicious emails can be examined using their headers, authentication results, and embedded URLs.

The project starts with a Python command-line tool that parses `.eml` email files and extracts information that can support an initial security assessment.

The goal is to build practical skills in email analysis, Python programming, and security-focused problem-solving.

## Current Features

- Parse `.eml` email files using Python's built-in email library
- Extract sender, subject, Reply-To, and Return-Path fields
- Display reported SPF, DKIM, and DMARC authentication results
- Extract HTTP and HTTPS URLs from plain-text email content
- Display the hostnames of extracted URLs
- Handle missing files and missing email headers

## Planned Features

- Automated tests using pytest
- URL and domain analysis
- Detection of sender and Reply-To mismatches
- Rule-based phishing indicators
- Risk classification with explanations
- Documented email analysis case studies
- Structured JSON analysis reports

Features listed here are planned and may change as the project develops.

## Technologies

- **Python 3**
- **Git and GitHub**
- **Python standard library**

Additional technologies may be introduced as the project evolves.

## Getting Started

### Requirements

- Python 3.10 or newer
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/Lehk1s/phishing-analysis-lab.git
cd phishing-analysis-lab
```

### Run the Analyzer

Place an email sample in the `samples/` directory and run:

```bash
python src/analyze_email.py samples/sample_email.eml
```

The program displays the extracted email headers, reported authentication results, and URLs found in plain-text message content.

## Example Output

```text
=== Email Analysis ===
Subject: Example password reset notification
From: Example Support <support@example.com>
Reply-To: reply@example.net
Return-Path: Not provided

=== Authentication Results ===
example.com; spf=pass; dkim=pass; dmarc=pass

=== URLs ===
URL: https://example.com/account
Hostname: example.com
```

Output depends on the contents of the analyzed email.

## Security and Limitations

This project is intended for educational purposes and defensive security analysis.

- Authentication results are extracted from email headers and are not independently verified by the tool.
- A reported SPF, DKIM, or DMARC result does not by itself establish whether an email is legitimate.
- Extracted URLs and domains are not automatically visited or independently verified.
- The current version extracts information but does not independently classify emails as phishing.
- A suspicious indicator does not necessarily mean that an email is malicious.

Only use email samples that you are authorized to analyze. Avoid committing personal information, confidential emails, credentials, or live malicious payloads to the repository.

## Learning Objectives

- Understand the structure of email messages and headers
- Explore SPF, DKIM, and DMARC authentication
- Practice parsing structured data with Python
- Learn to identify and document potential phishing indicators
- Develop secure coding, testing, and documentation practices

## Project Status

**Status:** Initial development

This project is being developed incrementally, starting with email parsing and progressing toward a rule-based phishing triage tool.