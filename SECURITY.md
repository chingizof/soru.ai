# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the severity of the vulnerability.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of Soru.ai seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Where to Report

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to: **security@soru.ai**

Alternatively, you can use GitHub's private vulnerability reporting feature:
1. Go to the repository's Security tab
2. Click "Report a vulnerability"
3. Fill in the details

### What to Include

Please include the following information in your report:

- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 5 business days
- **Resolution**: Depends on severity and complexity

### What to Expect

1. **Acknowledgment**: We'll acknowledge receipt of your report
2. **Investigation**: We'll investigate and validate the issue
3. **Fix Development**: We'll develop a fix if the issue is confirmed
4. **Disclosure**: We'll coordinate disclosure with you
5. **Credit**: We'll credit you in our security advisory (unless you prefer to remain anonymous)

## Security Best Practices

### For Users

1. **Never commit API keys**: Use environment variables
2. **Keep dependencies updated**: Run `pip install -U -r requirements.txt` regularly
3. **Use HTTPS**: Always access the application over HTTPS in production
4. **Secure your .env file**: Never share or commit this file
5. **Regular updates**: Keep Soru.ai updated to the latest version

### For Developers

1. **Input validation**: Always validate and sanitize user input
2. **API key protection**: Never hardcode credentials
3. **Dependency scanning**: Regularly scan for vulnerable dependencies
4. **Code review**: Review security-critical code changes carefully
5. **Least privilege**: Grant minimum necessary permissions

## Known Security Considerations

### API Keys

- Store all API keys in `.env` file
- Never commit `.env` to version control
- Use separate keys for development and production
- Rotate keys regularly

### File Uploads

- Only accept image files for OCR processing
- Validate file types and sizes
- Clean up uploaded files after processing
- Implement rate limiting to prevent abuse

### External APIs

- Use HTTPS for all API calls
- Validate API responses
- Implement timeout and retry logic
- Handle API errors gracefully

## Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the problem and determine affected versions
2. Audit code to find similar problems
3. Prepare fixes for all supported versions
4. Release patches as soon as possible

## Security Updates

Security updates will be released as patch versions (e.g., 1.0.1, 1.0.2).

Subscribe to our releases to get notified:
- Watch the repository on GitHub
- Follow our [Twitter](https://twitter.com/soruai)
- Join our [Discord](https://discord.gg/soruai)

## Security Hall of Fame

We appreciate the efforts of security researchers who responsibly disclose vulnerabilities:

<!-- List will be updated as reports are received and resolved -->

*No vulnerabilities reported yet*

## Contact

For any security concerns, contact:
- Email: security@soru.ai
- PGP Key: [Available on request]

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Reflex Security Guidelines](https://reflex.dev/docs/security/)

---

**Last Updated**: November 2024

