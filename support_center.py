import streamlit as st
import smtplib
from email.mime.text import MIMEText

# SEND EMAIL FUNCTION
def send_email(user_name, user_email, message_text):
    """Send the support message to the configured email account."""
    gmail_user = st.secrets["email"]["address"]
    gmail_pass = st.secrets["email"]["password"]

    msg = MIMEText(
        f"New Support Request Received!\n\n"
        f"From: {user_name}\n"
        f"Email: {user_email}\n\n"
        f"Message:\n{message_text}"
    )
    msg["Subject"] = "Interactive Trading Simulator"
    msg["From"] = gmail_user
    msg["To"] = gmail_user

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(gmail_user, gmail_pass)
        server.sendmail(gmail_user, gmail_user, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

# SUPPORT CENTER
def run():
    st.title("🗨️ Support Center")
    st.write("Need help or have a question? Check the FAQs below or send a message using the form.")

    st.markdown("----")

    # FREQUENTLY ASKED QUESTIONS
    st.markdown("""
    ### ❓ Frequently Asked Questions
    """)
    with st.expander("How do I load my own stock CSV file in the Trading Simulator?"):
        st.markdown("""
        To load your own stock CSV file, go to the 'Trading Simulator' section and click on the 'Upload CSV' button. 
        Use the sidebar upload feature to select your CSV file. Ensure it contains Date, Open, High, Low, and Close columns.
        """)
    with st.expander("Can I reset my trading simulator portfolio in the simulator?"):
        st.markdown("""
        Yes! Use the reset button in the Trading Simulator page to reset cash, positions, and trade history.
        """)
    with st.expander("How do I save or export my trade history from the Trading Simulator?"):
        st.markdown("""
        You can export your trade history as a CSV file by hovering over the top right corner of the 'Trading History' table and clicking the download button.
        """)
    with st.expander("Is this real trading?"):
        st.markdown("""
        No, this is a trading simulator designed for educational purposes. It allows you to practice trading strategies without risking real money.
        """)
    with st.expander("What should I do if I encounter a bug or issue with the app?"):
        st.markdown("""
        If you encounter a bug, please report it using the contact form below. Provide as much detail as possible about the issue.
        """)
    
    st.markdown("""---""")

    # CONTACT SUPPORT
    st.markdown("### 📬 Contact Support")
    with st.form("support_form"):
        col1, col2 = st.columns(2)
        with col1:
            user_name = st.text_input("Your Name")
        with col2:
            user_email = st.text_input("Your Email")

        subject = st.text_input("Subject (optional)", value="General Inquiry")
        user_message = st.text_area("Message", height=150)

        submitted = st.form_submit_button("Send Message")

        if submitted:
            if not user_name.strip() or not user_email.strip() or not user_message.strip():
                st.error("Please fill in your name, email, and message before sending.")
            else:
                with st.spinner("Sending your message..."):
                    success = send_email(user_name, user_email, subject, user_message)
                if success:
                    st.success("Your message has been sent successfully! Check your email for a response.")
                    st.experimental_rerun()
                else:
                    st.error("There was an error sending your message. Please try again later.")
