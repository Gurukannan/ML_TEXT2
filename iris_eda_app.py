import streamlit as st 
import enchant

def main():
	""" A simple Iris EDA App """

	st.title("Iris EDA App with streamlit")
	st.subheader("Streamlit is Cool")
	message = st.text_area("Enter Text","Type Here ..")
	if st.button("Analyze"):
# Using 'en_US' dictionary 
		d = enchant.Dict("en_US") 
		word = message
		d.check(word)
		df=d.suggest(word)
		st.json(df)

if __name__ == '__main__':
	main()