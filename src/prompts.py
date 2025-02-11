instruction_prompt = '''
                
### **Instruction:**  
Your task is to generate a structured and concise legal synthesis table based on a given statute or regulation. Follow these precise guidelines:  

1. **Provide a clear, succinct summary** of the legal concept in non-legal language.  
2. **Create a table** with four structured columns:  
   - **First Column (Legal Synthesis):** Explain the legal concept in simple, plain text without legal jargon.  
   - **Second Column (Business Requirements):** Provide the **exact** statutory or regulatory language outlining the requirements. Ensure it follows a "must do this" / "cannot do that" structure.  
   - **Third Column (Translated Business Requirements):** Rewrite each requirement in the second column into simple, clear, non-legal text.  
   - **Fourth Column (Key Points - Requirements, Permissions, Prohibitions):** Break down the requirements into three bullet points:  
     - **Requirement:** What must be done.  
     - **Permission:** What is allowed but requires permission or additional requirements.  
     - **Prohibition:** What is explicitly not allowed.  

3. **Ensure consistency** in formatting, parallel structure, and clarity across all columns.  
4. **Double-check the formatting** to ensure proper Markdown usage.  
5. **Use precise, simple language** while maintaining the integrity of the legal requirements.  

---

### **Table Format Example:**  

```markdown
| **Legal Synthesis** | **Business Requirements** | **Translated Business Requirements** | **Key Points (Requirements, Permissions, Prohibitions)** |
|---------------------|-------------------------|--------------------------------------|----------------------------------------------------------|
| [Explain the legal concept simply] | [Exact language from the statute/regulation] | [Translate each requirement into clear, non-legal text] | - **Requirement:** [What must be done] <br> - **Permission:** [What is allowed] <br> - **Prohibition:** [What is not allowed] |
                
                
                
'''
