instruction_prompt = '''
                ### Instruction:
                1. Provide a succinct and concise answer to the user's question in clear, non-legal language.
                2. Create a table with three columns:
                   - **First Column:** Explain the legal interpretation in simple, plain text without legal jargon.
                   - **Second Column:** Translate the text into clear actionable business requirements in bullet points.
                   - **Third Column:** Provide three bullet points explaining requirements, permissions, and prohibitions in clear language.
                3. Double-check the format to ensure it meets these specifications.
                4. Ensure the language is simple, precise, and free of complex terminology.
                5. Ensure that Markdown is properly formatted.

                **Table Format Example:**

                | Legal Interpretation (Plain Text) | Business Requirements (Simple Terms) | Key Points (Requirements, Permissions, Prohibitions) |
                |------------------------------------|--------------------------------------|-----------------------------------------------------|
                | [Explain legal concept simply]     | [Translate into actionable business requirements in bullet points] | - **Requirement:** [What must be done]  <br> - **Permission:** [What is allowed]  <br> - **Prohibition:** [What is not allowed] |
                    '''
