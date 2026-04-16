# Security Policy

This document outlines how we handle security vulnerabilities and maintain the security of the openclaw-workspace-sowork project.

## Reporting a Vulnerability

**⚠️ DO NOT** create public GitHub issues to report security vulnerabilities.

Instead, please report security issues responsibly by:

1. **Email**: Send details to the project maintainer
2. 2. **GitHub Security Advisory**: Use GitHub's private vulnerability reporting feature
   3. 3. **Response Time**: We aim to respond to reports within 48 hours
     
      4. ### What to Include in a Report
     
      5. - Clear description of the vulnerability
         - - Steps to reproduce (if applicable)
           - - Potential impact
             - - Suggested fix (if you have one)
               - - Your contact information
                
                 - ## Security Considerations
                
                 - ### Data Isolation & Memory Protection
                
                 - - **MEMORY.md** is intentionally security-gated and only loads in main sessions
                   - - MEMORY.md is **never loaded** in group chats or sub-agent sessions
                     - - The `AGENTS.md` boot sequence explicitly gates: "Main session only: Read MEMORY.md"
                       - - All memory files are stored in `memory/` directory with separate access controls
                        
                         - ### Workspace Security
                        
                         - - All workspace files are plain Markdown — no executable code
                           - - No external API calls in core workspace files
                             - - No embedded scripts or potential injection vectors
                               - - Configuration is explicit and auditable
                                
                                 - ### Credentials & Sensitive Data
                                
                                 - - **Never commit** API keys, tokens, or credentials
                                   - - **Never commit** personal memory files or conversation history
                                     - - All sensitive files are covered by `.gitignore`
                                       - - Use environment variables for runtime secrets (see TOOLS.md)
                                        
                                         - ### Five-Layer Learning Security
                                        
                                         - The workspace implements Hermes-inspired five-layer learning with security at each level:
                                        
                                         - 1. **Enterprise Level** (`learn/enterprise/`) - Organization-wide patterns (no PII)
                                           2. 2. **Brand Level** (`learn/brand/`) - Brand guidelines and positioning (public-safe)
                                              3. 3. **Department Level** (`learn/department/`) - Team-specific knowledge (internal-only)
                                                 4. 4. **Team Level** (`learn/team/`) - Direct team learnings (member-access)
                                                    5. 5. **Personal Level** (`learn/personal/`) - Individual patterns (private-only)
                                                      
                                                       6. Each level has:
                                                       7. - Access control markers (`@public`, `@internal`, `@private`)
                                                          - - Version tracking for auditing
                                                            - - Separation from MEMORY.md (confidential context)
                                                             
                                                              - ## Dependency & Supply Chain Security
                                                             
                                                              - - This workspace has **zero production dependencies** — it's pure configuration
                                                                - - No npm packages, pip packages, or external binaries required
                                                                  - - Installation is purely file-copy based
                                                                    - - No automated package updates needed
                                                                     
                                                                      - ## GitHub Repository Settings
                                                                     
                                                                      - We maintain the following security measures:
                                                                     
                                                                      - - ✅ Secret scanning alerts enabled
                                                                        - - ✅ Dependabot alerts disabled (zero dependencies)
                                                                          - - ✅ Code scanning ready (optional, template-based)
                                                                            - - ⚠️ Private vulnerability reporting (recommended for users to enable)
                                                                              - - ✅ Branch protection on main (enforced in settings)
                                                                               
                                                                                - ## Workspace File Security
                                                                               
                                                                                - | File | Contains | Risk Level | Security |
                                                                                - |------|----------|-----------|----------|
                                                                                - | AGENTS.md | Boot logic, routing | Low | Auditable, no execution |
                                                                                - | SOUL.md | Brand identity | Low | Non-sensitive config |
                                                                                - | MEMORY.md | Context & history | **HIGH** | Security-gated, main-session only |
                                                                                - | TOOLS.md | API configs | Medium | Env-var based, no hardcoding |
                                                                                - | USER.md | Team preferences | Low | General knowledge, no PII |
                                                                                - | memory/* | Session logs | **HIGH** | Local storage, not version-controlled |
                                                                                - | outputs/* | Agent output | Medium | May contain generated content |
                                                                               
                                                                                - ## Incident Response
                                                                               
                                                                                - If a security incident is discovered:
                                                                               
                                                                                - 1. Report it via the vulnerability disclosure process above
                                                                                  2. 2. We will investigate and provide an update within 48 hours
                                                                                     3. 3. A patch will be released if needed
                                                                                        4. 4. We will credit the reporter (unless they prefer anonymity)
                                                                                          
                                                                                           5. ## Known Limitations
                                                                                          
                                                                                           6. - This is a **configuration template**, not a security framework
                                                                                              - - Users are responsible for securing their own `.env` files and API keys
                                                                                                - - Deploy with proper authentication in production environments
                                                                                                  - - Review all customizations for security implications
                                                                                                   
                                                                                                    - ## Best Practices for Users
                                                                                                   
                                                                                                    - 1. **Environment Variables**: Store all credentials in `.env` files (ignored by git)
                                                                                                      2. 2. **Access Control**: Use OS-level file permissions on `memory/` and `MEMORY.md`
                                                                                                         3. 3. **Regular Audits**: Review workspace files for accidental credential leakage
                                                                                                            4. 4. **MEMORY Isolation**: Ensure AGENTS.md security gates are not bypassed
                                                                                                               5. 5. **Deployment**: Use proper secret management in production (e.g., GitHub Secrets, HashiCorp Vault)
                                                                                                                 
                                                                                                                  6. ## Compliance
                                                                                                                 
                                                                                                                  7. This workspace is designed to support:
                                                                                                                 
                                                                                                                  8. - **GDPR**: Separate data layers prevent PII leakage
                                                                                                                     - - **SOC 2**: Auditable configuration, no hidden operations
                                                                                                                       - - **ISO 27001**: Clear access controls and logging
                                                                                                                         - - **Internal policies**: Customizable via USER.md and AGENTS.md
                                                                                                                          
                                                                                                                           - ## Questions?
                                                                                                                          
                                                                                                                           - For security questions that are not vulnerability reports, please open a regular GitHub Issue with the `security` label.
