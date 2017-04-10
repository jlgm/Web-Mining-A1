package Stemer;

import java.io.File;
import java.io.FileFilter;
import java.io.FileReader;
import java.io.IOException;
import java.io.StringReader;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.analysis.standard.StandardTokenizer;
import org.apache.lucene.analysis.tokenattributes.CharTermAttribute;
import org.apache.lucene.analysis.tokenattributes.OffsetAttribute;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.CorruptIndexException;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;
import org.apache.lucene.analysis.PorterStemFilter;
import org.apache.lucene.analysis.TokenStream;
import org.apache.lucene.analysis.WhitespaceAnalyzer;


public class Stemer {
	public static String tokenizeStopStem(String input) {

		TokenStream tokenStream = new StandardTokenizer(
				Version.LUCENE_36, new StringReader(input));
		tokenStream = new PorterStemFilter(tokenStream);

		StringBuilder sb = new StringBuilder();
		OffsetAttribute offsetAttribute = tokenStream.addAttribute(OffsetAttribute.class);
		CharTermAttribute charTermAttr = tokenStream.getAttribute(CharTermAttribute.class);
		try{
			while (tokenStream.incrementToken()) {
				if (sb.length() > 0) {
					sb.append(" ");
				}
				sb.append(charTermAttr.toString());
			}
		}
		catch (IOException e){
			System.out.println(e.getMessage());
		}
		return sb.toString();
	}
	
	

}
