<h1>Insurance Parser API</h1>

<p>
  This is an LLM-powered document processing system developed for <strong>HackRx 6.0 (Bajaj Finserv Health Limited)</strong>. 
  It processes natural language queries and retrieves relevant information from large unstructured documents such as policy documents, contracts, and emails.
</p>

<h2>Features</h2>

<ul>
  <li><strong>Retrieval-Augmented Generation (RAG) Pipeline:</strong> Combines document retrieval with LLM-powered answer generation for accurate and contextual results.</li>
  <li><strong>Document Chunking:</strong> Splits large documents into manageable chunks for efficient search.</li>
  <li><strong>Semantic Search with ChromaDB:</strong> Uses embeddings to store and query document content.</li>
  <li><strong>Gemini LLM Integration:</strong> Generates human-like, context-aware responses.</li>
  <li><strong>FastAPI Backend:</strong> Exposes an API endpoint for document and query processing.</li>
  <li><strong>Bearer Token Authentication:</strong> Secured API access with token-based authorization.</li>
</ul>

<h2>Tech Stack</h2>

<ul>
  <li><strong>Python 3.9</strong></li>
  <li><strong>FastAPI</strong> – API framework</li>
  <li><strong>LangChain</strong> – Chunking & embeddings pipeline</li>
  <li><strong>Google Generative AI</strong> – Gemini LLM for embeddings & answers</li>
  <li><strong>ChromaDB</strong> – Vector database for semantic search</li>
</ul>

<h2>Installation</h2>

<p>Follow the steps below to set up the project locally.</p>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/SatCodes12/InsuranceParserSegFault.git
cd InsuranceParserSegFault
</code></pre>

<ol start="2">
  <li>Create a virtual environment and activate it:</li>
</ol>

<pre><code>python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
</code></pre>

<ol start="3">
  <li>Install the dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<h2>Set Up Environment Variables</h2>

<p>Create a <code>.env</code> file in the root directory and add the following:</p>

<pre><code>GOOGLE_API_KEY=your_google_api_key
BEARER_TOKEN=your_bearer_token
</code></pre>

<p>
  Replace <code>your_google_api_key</code> and <code>your_bearer_token</code> with valid values.
</p>

<h2>Running the API</h2>

<p>Once the environment is configured, start the FastAPI server:</p>

<pre><code>uvicorn main:app --reload
</code></pre>

<p>
  By default, the API will be available at:
  <a href="http://localhost:8000/api/v1/hackrx/run" target="_blank">http://localhost:8000/api/v1/hackrx/run</a>
</p>

<h2>Authentication</h2>

<p>The API uses Bearer Token Authentication for all protected routes.</p>

<p>Include the following header in your requests:</p>

<pre><code>Authorization: Bearer your_bearer_token
</code></pre>

<p>
  Replace <code>your_bearer_token</code> with the token set in your <code>.env</code> file.
</p>

<h2>Input & Output Format</h2>

<h3>Request Format</h3>

<p>Send a POST request to the API endpoint with the following JSON structure:</p>

<pre><code>{
  "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
  "questions": [
    "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
    "What is the waiting period for pre-existing diseases (PED) to be covered?",
    "Does this policy cover maternity expenses, and what are the conditions?",
    "What is the waiting period for cataract surgery?",
    "Are the medical expenses for an organ donor covered under this policy?",
    "What is the No Claim Discount (NCD) offered in this policy?",
    "Is there a benefit for preventive health check-ups?",
    "How does the policy define a 'Hospital'?",
    "What is the extent of coverage for AYUSH treatments?",
    "Are there any sub-limits on room rent and ICU charges for Plan A?"
  ]
}
</code></pre>

<h3>Response Format</h3>

<p>The API will respond with a JSON object containing an array of answers, in the same order as the questions:</p>

<pre><code>{
  "answers": [
    "The grace period for premium payment to maintain continuity of benefits is 30 days.",
    "Coverage for pre-existing diseases begins after thirty-six months of continuous coverage from the first policy's inception, provided the condition was declared and accepted at the time of application.",
    "Yes, maternity expenses are covered, including pre-natal and post-natal hospitalization and newborn vaccination, subject to a twenty-four month waiting period which may be waived for accidental delivery, miscarriage, or abortion, and is limited to two deliveries or terminations over the policy's lifetime and one per policy period, with specific limits for normal and caesarean deliveries.",
    "Cataract surgery is covered after a waiting period of two years.",
    "Medical expenses for an organ donor are covered for in-patient hospital care, contingent on the insured person's organ transplant claim being admitted under in-patient treatment, with exclusions for pre- and post-hospitalization, organ acquisition, experimental procedures, post-harvesting complications, and transportation or preservation.",
    "A No Claim Discount of a flat 5% is offered on the base premium upon renewal for one-year policies if no claims were reported, and for multi-year policies, the aggregated discount for claim-free years is also up to 5% of the total base premium for the policy term.",
    "Yes, expenses for health check-ups are reimbursed at the end of every two continuous policy years, provided the policy has been continuously renewed without a break, and are subject to the limits specified in the Table of Benefits.",
    "A hospital is defined as an institution for in-patient and day care treatment of diseases or injuries, registered with local authorities or meeting specific criteria including qualified nursing staff, a minimum number of inpatient beds, round-the-clock medical practitioners, an equipped operation theatre, and patient record maintenance.",
    "AYUSH treatments, encompassing Ayurveda, Yoga and Naturopathy, Unani, Siddha, and Homeopathy systems, are covered when received in a recognized AYUSH Hospital or AYUSH Day Care Centre that meets the specified criteria.",
    "Yes, room charges and intensive care unit charges per day are payable up to a specified limit for Plan A, unless the treatment is for a listed procedure within a Preferred Provider Network as a package."
  ]
}
</code></pre>

<h2>Repository</h2>

<p>
  GitHub Repository: <a href="https://github.com/SatCodes12/InsuranceParserSegFault" target="_blank">https://github.com/SatCodes12/InsuranceParserSegFault</a>
</p>
