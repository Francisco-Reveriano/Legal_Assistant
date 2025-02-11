instruction_prompt = '''
## **Refined GPT Prompt**  

### **Instructions**  

Your task is to extract and format regulatory information into a structured Markdown table for the question asked with four specific columns. Follow these detailed guidelines:  

1. **Column 1 – Legal Synthesis:**  
   - Provide a **single, concise paragraph** summarizing the identified regulation.  
   - Use plain, non-technical language to clearly explain the overall legal concept.  

2. **Column 2 – Business Requirements (Exact Legal Text):**  
   - Extract a comprehensive list of **all business requirements** from the statute or regulation.  
   - Use the **exact wording** from the legal text.  
   - Each requirement must follow a **"must do this"** or **"cannot do that"** structure.  
   - **Each distinct business requirement must occupy its own row** in the table.  

3. **Column 3 – Simplified Interpretation:**  
   - For every requirement listed in Column 2, provide a **clear and simplified explanation** in plain English.  
   - Remove legal jargon while maintaining the original meaning.  
   - The interpretation should be **actionable and easy to understand**.  

4. **Column 4 – Detailed Breakdown (Requirements, Permissions, and Prohibitions):**  
   - For each business requirement, create a structured breakdown using three bullet points:  
     - **Requirement:** What must be done.  
     - **Permission:** What is allowed, provided specific conditions are met.  
     - **Prohibition:** What is explicitly not allowed.  
   - This breakdown must directly relate to the corresponding business requirement from Column 2.  

5. **Formatting and Structure:**  
   - Construct a **Markdown table** with **four columns**, as described above.  
   - Ensure that each row represents **one distinct business requirement**, maintaining a parallel structure across Columns 2, 3, and 4.  
   - Verify that the final Markdown output is **correctly rendered and properly aligned**.  

---

## **Example Output (Markdown)**  

```markdown
| Legal Synthesis | Business Requirements (Exact Legal Text) | Simplified Interpretation | Detailed Breakdown |
|-----------------|------------------------------------------|---------------------------|--------------------|
| [Insert a concise summary of the regulation in plain language.] | [Exact text of Requirement 1 from the statute/regulation.] | [Plain English explanation of Requirement 1.] | - **Requirement:** [What must be done.]<br>- **Permission:** [Actions allowed under conditions.]<br>- **Prohibition:** [Actions that are not allowed.] |
| [Insert a concise summary (or leave blank if already provided above).] | [Exact text of Requirement 2 from the statute/regulation.] | [Plain English explanation of Requirement 2.] | - **Requirement:** [What must be done.]<br>- **Permission:** [Actions allowed under conditions.]<br>- **Prohibition:** [Actions that are not allowed.] |

## **Additional Instructions**
1. **Double-check that table is properly formatted and aligned.**
2. **Make sure that prompt instructions are followed.**

## **Question**
Question: {question}
'''


def generate_prompt(question: str) -> str:
    """
    Generates a refined GPT prompt with the user's question inserted.

    :param question: The user's question to be inserted in the prompt.
    :return: The formatted instruction prompt with the question included.
    """
    instruction_prompt = f'''
## **Refined GPT Prompt**  

### **Instructions**  

Your task is to extract and format regulatory information into a structured Markdown table for the question asked with four specific columns. Follow these detailed guidelines:  

1. **Column 1 – Legal Synthesis:**  
   - Provide a **single, concise paragraph** summarizing the identified regulation.  
   - Use plain, non-technical language to clearly explain the overall legal concept.  

2. **Column 2 – Business Requirements (Exact Legal Text):**  
   - Extract a comprehensive list of **all business requirements** from the statute or regulation.  
   - Use the **exact wording** from the legal text.  
   - Each requirement must follow a **"must do this"** or **"cannot do that"** structure.  
   - **Each distinct business requirement must occupy its own row** in the table.  

3. **Column 3 – Simplified Interpretation:**  
   - For every requirement listed in Column 2, provide a **clear and simplified explanation** in plain English.  
   - Remove legal jargon while maintaining the original meaning.  
   - The interpretation should be **actionable and easy to understand**.  

4. **Column 4 – Detailed Breakdown (Requirements, Permissions, and Prohibitions):**  
   - For each business requirement, create a structured breakdown using three bullet points:  
     - **Requirement:** What must be done.  
     - **Permission:** What is allowed, provided specific conditions are met.  
     - **Prohibition:** What is explicitly not allowed.  
   - This breakdown must directly relate to the corresponding business requirement from Column 2.  

5. **Formatting and Structure:**  
   - Construct a **Markdown table** with **four columns**, as described above.  
   - Ensure that each row represents **one distinct business requirement**, maintaining a parallel structure across Columns 2, 3, and 4.  
   - Verify that the final Markdown output is **correctly rendered and properly aligned**.  

---

## **Additional Instructions**
1. **Double-check that table is properly formatted and aligned.**
2. **Make sure that prompt instructions are followed.**

## **Question**
Question: {question}
'''
    return instruction_prompt
