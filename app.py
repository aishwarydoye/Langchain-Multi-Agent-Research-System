import streamlit as st
from src.pipelines.pipeline import run_research_pipeline

# Page setup
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔍",
    layout="wide"
)

# Custom header styling
st.title("🤖 Multi-Agent Research System")
st.caption("Powered by LangChain, Groq, Tavily & Trafilatura")

with st.sidebar:
    st.header("⚙️ System Overview")
    st.markdown("""
    This system runs a 4-step multi-agent research pipeline:
    1. **Search Agent**: Gathers recent & relevant web resources.
    2. **Reader Agent**: Scrapes deep content from top URLs.
    3. **Writer Agent**: Synthesizes findings into a structured report.
    4. **Critic Agent**: Reviews the report and provides an evaluation score.
    """)
    

# Search input form
query = st.text_input(
    "Enter a research topic:",
    placeholder="e.g. Impact of AI on semiconductor supply chains",
    help="Enter any topic you'd like the multi-agent team to research."
)

col1, col2 = st.columns([1, 5])
with col1:
    start_research = st.button("🚀 Start Research", type="primary", use_container_width=True)

if start_research:
    if not query.strip():
        st.warning("Please enter a research topic first.")
    else:
        with st.status("Executing Research Pipeline...", expanded=True) as status:
            try:
                st.write("🔍 Running multi-agent pipeline...")
                results = run_research_pipeline(query.strip())
                status.update(label="Research Complete!", state="complete", expanded=False)
                
                # Main outputs in tabs
                tab_report, tab_critic, tab_raw = st.tabs(["📝 Final Report", "⚖️ Critic Evaluation", "🔎 Raw Pipeline Data"])

                with tab_report:
                    st.subheader("Research Report")
                    st.markdown(results.get("report", "No report generated."))
                    
                    # Download button for the report
                    st.download_button(
                        label="📥 Download Report (.md)",
                        data=results.get("report", ""),
                        file_name=f"research_report_{query.strip().replace(' ', '_')[:30]}.md",
                        mime="text/markdown"
                    )

                with tab_critic:
                    st.subheader("Critic Review & Feedback")
                    st.markdown(results.get("feedback", "No feedback available."))

                with tab_raw:
                    st.subheader("Step 1: Search Results")
                    with st.expander("View Search Agent Output", expanded=False):
                        st.markdown(results.get("search_results", "No search data."))

                    st.subheader("Step 2: Scraped Web Content")
                    with st.expander("View Reader/Scraper Output", expanded=False):
                        st.markdown(results.get("scraped_content", "No scraped data."))

            except Exception as e:
                status.update(label="An error occurred", state="error", expanded=True)
                st.error(f"Error during research execution: {e}")
