import os, re, json
definitions = """<strong>Corpus linguistics</strong>  is a scientific method of language analysis.
<strong>Statistics</strong> is a discipline which helps us make sense of quantitative data; in other words, statistics is a ‘science of collecting and interpreting data’ (Diggle & Chetwynd 2011: vii) that can be counted, measured or quantified in some way.
<strong>Mean</strong> is an average value which represents a whole range of values, and is calculated by dividing the sum of all values by the number of cases.
<strong>Regression line</strong> is an example of a mathematical representation of complex linguistic reality shown on a graph.
<strong>Corpus </strong> is a specific form of linguistic data. It is a collection of written texts or transcripts of spoken language that can be searched by a computer using specialized software.
<strong>Sample </strong> is a small subset of the language production of interest.
<strong>Population</strong> is all language of interest to the researcher.
<strong>Dataset</strong> is a series of corpus-based findings that can be statistically analysed. It is a systematic collection of individual results that can be stored in the form of a table in a spreadsheet program.
<strong>Variable</strong> is something that can vary and take on different values. For example, a speaker's age.
<strong>Linguistic variables</strong> capture frequencies of linguistic features of interest.
<strong>Explanatory variables</strong> are sometimes called 'independent variables' or 'predictor variables' and capture contexts in which the linguistic features appear. They can be, for example, the genre/register of a text, the speaker's age or their gender.
<strong>Nominal variable</strong> has values that represent different categories into which the cases in a dataset can be grouped. There is no order or hierarchy between the categories.
<strong>Ordinal variable</strong> also groups values into distinct categories, but the categories can be ordered according to some inherent hierarchy. For example, speaker's proficiency can be ordered from beginners to advanced.
<strong>Scale variable</strong> is a quantitative variable because it can take on any value on a scale showing the quantity of a particular feature. They can also be added, subtracted, multiplied and divided because they represent measurable quantities.
<strong>Frequency distribution</strong> of a variable provides information about the values a variable takes and their frequencies.
<strong>Normal distribution</strong> is one of the common distributions often used in statistics. It is shaped like a symmetrical bell.
<strong>Outliers</strong> are extreme values which are very far from the others.
<strong>Rogue value</strong> is a measurement error which can be caused, for example, by mistyping.
<strong>Measure of central tendency</strong> provides one summary value for a series of values of a scale variable.
<strong>Median</strong> is the middle value in a series of values ordered from smallest to largest.
<strong>Dispersion</strong> is the spread of values of a variable in a dataset.
<strong>Range</strong> is the distance between the smallest and largest value.
<strong>Interquartile range</strong> is the interval between the lower and upper quartile- the lower and upper boundary of the 'middle bulk' of the values sorted from lowest to highest- and represents 50% of the values from the distribution excluding the median and the borders.
<strong>Standard deviation</strong> is the square root of the sums of squared distances of the individual values from the mean. It gives us an indication of the overall distance between individual values and the mean.
<strong>Statistical measure</strong> is a general term for any statistic we calculate.
<strong>Statistical test</strong> is a procedure in a branch of inferential statistics.
<strong>Inferential statistics</strong> is that which goes beyond the sample to infer something about the population.
<strong>Null hypothesis</strong> states that there is nothing special going on in the analysed corpus or corpora. For example, there is no difference between two (sub)corpora.
<strong>Statistically significant</strong> when the difference observed in a sample is likely to be a true difference in the population.
<strong>P-value</strong> is a probability value and one of the outcomes of a statistical test. It can be defined as the probability that the data would be at least as extreme as that observed if the null hypothesis were true.
<strong>Assumptions</strong> (of a statistical test) are conditions that should be met for the test to produce valid results.
<strong>Normality assumption</strong> presupposes that the frequency distribution of the linguistic variable does not deviate considerably from the normal distribution.
<strong>Confidence interval</strong> provides an estimation of the true value of a statistical measure or of a difference between two measures in the population.
<strong>Effect size</strong> is a standardized measure comparable across different studies. It expresses the practical importance of the effect observed in the corpus or corpora.
<strong>Representative</strong> is a descriptor of a sample when it has similar characteristics to the population it is drawn from.
<strong>Random sampling</strong> in language would be where each text ever produced and every spoken interaction that has ever taken place has the same chance of appearing in a sample. This is, however, impracticable.
<strong>Sampling frame</strong> is a set of categories from which corpus designers aim to collect an unbiased sample.
<strong>Bias</strong> is a systematic but often hidden deviation of the sample from the population.
<strong>Test sample bias</strong> is where only certain sections of texts are used in a sample- for example, only the beginnings of books.
<strong>Topic bias</strong> is where many texts in a corpus are on the same topic.
<strong>Non-coverage bias</strong> is when some texts are more 'visible' than others in a corpus because designers see them as more prototypical for some reason.
<strong>Traditional text type bias</strong> is a specific case of non-coverage bias where when selecting a sampling frame we are predisposed to see text types which have traditionally been included in language corpora as more salient.
<strong>Legal consideration bias</strong> is when many texts are selected because copyright does not apply.
<strong>Practicality bias</strong> is when texts- such as webpages- are chosen because they are easier to obtain than others.
<strong>Self-selection bias</strong> is a bias created when contributors are asked to provide texts on a voluntary basis. For example, in a situation where classroom students are asked to volunteer, we may end up with texts from highly motivated students which will not reflect the production of the whole class.
<strong>Web as corpus initiative</strong> is based on the observation that large quantities of interesting linguistic material have become available online, and by crawling the web we can build corpora that are larger than ever before.
<strong>Practical importance</strong> uses standardized statistical measures to express the size of the effect.
<strong>Research design</strong> is the type and format of the data that needs to be obtained from the corpus in order to answer the research question.
<strong>Whole corpus design</strong> is a type of research design in which the unit of analysis is usually the whole corpus.
<strong>Individual text/speaker design</strong> is a type of research design which enables us to trace the frequency of a linguistic feature in the individual texts or speakers.
<strong>Linguistic feature design</strong> is a type of research design which focuses on the linguistic feature as a single observation (case).
<strong>Boxplot</strong> is a type of graph which shows the distribution of data as well as extreme values. The inside of the box represents the interquartile range and the thick horizontal line in the box represents the median. The 'whiskers' above and below the box show the minimum and maximum values excluding outliers which are displayed outside the scope of the 'whiskers' as separate data points.
<strong>Histogram</strong> is a graph that shows the frequency distribution of a linguistic variable in the form of bars, each representing the frequency of values in the linguistic variable in a given interval or bin.
<strong>Scatterplot matrix</strong> is how multiple scatterplots are presented.
<strong>Token</strong> is a single occurrence of a word form in a text.
<strong>Type</strong> is a unique word form in a corpus.
<strong>Lemma</strong> is a group of all inflectional forms relating to one stem that belong to the same word class (Kučera & Francis 1967: 1)
<strong>Lexeme</strong> is a lemma with a particular meaning attached to it, which is necessary to distinguish polysemous words (words with multiple meanings)
<strong>Absolute frequency (AF)</strong> is the actual count of all occurrences of a particular word in a corpus.
<strong>Relative frequency (RF)</strong> is the absolute frequency divided by the number of tokens in the corpus, multiplied by the basis for normalization. It can also be considered as the mean frequency.
<strong>Hapaxes</strong> are types that occur only once in a corpus.
<strong>Zipf's Law</strong> is the principle of rapidly diminishing word frequency.
<strong>Sample standard deviation</strong> is calculated in almost the same way as standard deviation, however the sum of squared distances is divided not by the total number of corpus parts but by the total number of corpus parts minus 1.
<strong>Coefficient of variation</strong> describes the amount of variation relative to the mean relative frequency of a word or phrase in a corpus. It is calculated by dividing the standard deviation by the mean.
<strong>Juilliand's D</strong> is a measure of dispersion that builds on the coefficient of variation. It is equal to 1 - the coefficient of variation divided by the square of the number of corpus parts - 1.
<strong>Deviation of Proportions (DP)</strong> is a measure proposed by Gries (2008) which compares the expected distribution of a word or phrase in corpus parts with the actual distribution. It is equal to the sum of the absolute values of (observed - expected proportions) divided by 2.
<strong>Type/token ratio (TTR)</strong> expresses the proportion of types relative to the proportion of tokens. It is calculated by dividing the number of types in a text or corpus by the number of tokens.
<strong>Standardized type/token ratio (STTR)</strong> is a measure otherwise known as mean segmental type/token ratio. It is calculated by dividing a text into standard sized segments (e.g. 1000 words), calculating the TTR for each segment and then taking the mean value of the TTRs.
<strong>Moving average type/token ration (MATTR)</strong> also calculates the average of TTRs in same size segments. However, instead of dividing the text into successive non-overlapping segments, MATTR uses an overlapping window moving smoothly through the text. This is a more robust measure as it takes into account all possible segmentations.
<strong>Collocations</strong> are words that occur in combinations habitually in texts and corpora.
<strong>Association measures</strong> are statistical measures that calculate the strength of association between words based on different aspects of the co-occurrence relationship.
<strong>Node</strong> is a word that we want to search for and analyse.
<strong>Collocation window</strong> is a defined span around the node where we find the collocates.
<strong>Observed frequency of collocation</strong> is the frequency of co-occurrence.
<strong>Expected frequency of collocation</strong> is the product of establishing the random co-occurrence base-line, and can be calculated by multiplying node frequency by collocate frequency and dividing this by the number of tokens in the text or corpus.
<strong>Contingency tables</strong> show all possible combinations of word co-occurrence.
<strong>Directionality</strong> is when we consider the symmetry between a node and a collocate- whether the attraction to each word is neutral.
<strong>Collocation graph</strong> is a visual representation of the collocational relationship between a node and its collocates.
<strong>Collocation network</strong> is a network of linked collocations that starts with an initial node (N1) around which a set of first-order collocates is identified. Any of these collocates can be considered a new node with a new set of collocates, and the process can be repeated multiple times to create an extensive network.
<strong>Lockwords</strong> are words that occur with similar frequencies in two corpora that we compare.
<strong>Corpus of interest</strong> is compared with a baseline reference corpus using a statistical measure to identify words that are used either more or less often in one compared to the other.
<strong>Inter-rater agreement</strong> is an estimate of how reliable and consistent a coding is.
<strong>Judgement variable</strong> is a variable that involves categorization or evaluation of cases by the analyst that might bring an element of subjectivity into the study.
<strong>Raw agreement</strong> is a metric, often expressed as a percentage, which provides the proportion of agreement cases in all cases. It is calculated by dividing the cases of agreement by the total number of cases.
<strong>Stacked bar chart</strong> is a graphical representation of (relative) frequencies of a linguistic variable with multiple variants in different parts of a corpus.
<strong>Outcome variable</strong> is the linguistic variable of interest.
<strong>Lexico-grammatical frame/envelope of variation/variable context</strong> identifying all contexts in which the linguistic variable operates.
<strong>Ambient linguistic variables</strong> can appear in any possible context and do not have a clearly defined lexico-grammatical frame.
<strong>Cross-tabulation</strong> is a technique which examines the relationship between categorical variables.
<strong>Categorical variables</strong> are nominal and ordinal variables.
<strong>Cross-tabulation tables</strong> are created by cross-plotting of one linguistic variable and one or more explanatory variables.
<strong>Mosaic plot</strong> turns the frequency information into the size of the areas in the plot. It also displays the proportions of the categories.
<strong>Chi-squared</strong> is a test that can be used for statistical significance in cross-tabulation.
<strong>Independence of observations </strong> is the assumption that every observation is independent of another.
<strong>Log-likelihood test</strong> measures statistical significance.
<strong>Probability ratio</strong> is a ratio of two probabilities from the cross-tab table comparing the probability of a particular linguistic outcome occurring in one context type relative to the same outcome occurring in another context type. It is calculated by dividing the probability of the outcome of interest in context 1 by the probability of the outcome of interest in context 2.
<strong>Odds ratio</strong> uses odds instead of probabilities. An odds ratio larger than 1 indicates that the odds of the outcome of interest occurring in the context of interest are larger than those of the same outcome occurring in the baseline context.
<strong>Logistic regression</strong> is a statistical technique that uses explanatory variables (which can be categorical or scale) to estimate their effect on the linguistic variable (which must be categorical).
<strong>Mixed-effect modelling</strong> is when we build a model from the data which best predicts the outcome variable, taking into account both so-called fixed and random effects.
<strong>Collinearity</strong> is characterised by high correlation between predictor variables.
<strong>Linearity</strong> means that the relationship between variables can be captured by a (regression) line.
<strong>Curvilinear</strong> means that the relationship between variables can be captured by a curve.
<strong>Baseline values</strong> are values against which the model compares the effects of the predictor(s) on the outcome.
<strong>Parsimonious model</strong> is a model that explains as much variation in the data as possible with as little data as possible.
<strong>Block entry</strong> is a way of deciding which relevant variables to put in the model by deciding a priori based on previous literature and linguistic theory, running the analysis then leaving in only the variables which have a statistically significant effect.
<strong>Step-wise entry</strong> is where we let the statistical software add or remove variables step-by-step until the information criterion is called AIC of the model is no further improved.
<strong>Forward</strong> is a procedure in step-wise entry that starts with no predictor variables in the model and keeps adding variables one-by-one.
<strong>Backward</strong> procedure in step-wise entry starts with a model which includes all available variables and deletes them one-by-one.
<strong>Hybrid</strong> procedure combines forward and backward techniques, adding and deleting predictors depending on reassessment of the model at each stage.
<strong>Baseline model</strong> includes no predictors and is used only as a reference point for more complex models.
<strong>Standard errors</strong> express how accurately the estimates reflect the value in the population- the smaller the better.
<strong>AIC (Akaike information criterion)</strong> is used to establish which model is the most efficient by reaching significance with as few variables as possible. When comparing two models based on the same dataset, the smaller the AIC, the better the dataset.
<strong>Interactions</strong> are specific predictor combinations which can, in some cases, have a significant impact on the outcome.
<strong>Intercept</strong> is a baseline value in the model estimating the situation where all predictors are at their baseline values.
<strong>Odds   </strong> are a unit used to measure the effect of the predictors, and can be calculated by dividing the probability of the outcome by the probability of not the outcome.
<strong>Log odds</strong> are also used to measure the effect of the predictors, and are calculated by taking the natural logarithm of odds.
<strong>Dummy variables</strong> are combinations of categorical predictors and their non-baseline values.
<strong>Log odds ratios</strong> take the natural logarithm of odds ratios and are useful for internal operation of logistic regression.
<strong>Wald's z</strong> is a significance statistic computed by dividing the estimate with its standard error.
<strong>Binomial logistic regression</strong> is a logistic regression with an outcome variable with two categories.
<strong>Multinomial logistic regression</strong> follows the same principles as binomial regression, but the comparisons are somewhat more complex.
<strong>Correlation</strong> measures whether two ordinal or scale variables are related by looking at the extent to which they covary. In other words, looking at if one variable increases, the other increases, decreases or stays the same.
<strong>Positive correlation</strong> is when an increase in the values of the first variable also means an increase in the values of the second variable.
<strong>Negative correlation</strong> is when one variable increases the other decreases.
<strong>Pearson's correlation</strong> is designed to work with scale variables. It expresses the amount of covariance (variation that the variables have in common) in the data in terms of the standard deviations of the two variables in question.
<strong>Euclidean distance</strong> is the shortest distance between one point (A) and another point (B) via a direct line between the two points.
<strong>Manhattan distance</strong> is when the distance between (A) and (B) is calculated by following the grids at right angles, and is more robust when dealing with outliers.
<strong>Hierarchical agglomerative cluster analysis</strong> is a type of cluster analysis typically used in corpus linguistics for non-diachronic data. We take the individual data points and in a step-by-step (hierarchical) procedure join (i.e. agglomerate) the closest ones until we create one large cluster containing all the data points.
<strong>Hierarchical tree plot (or dendrogram)</strong> can display the results of a cluster procedure, showing the individual steps (clusters) as smaller branches gradually converging into one large cluster.
<strong>Registers</strong> are functionally defined types of language use.
<strong>Multidimensional analysis</strong> is a complex procedure developed by Biber (1988) that deals with a large number of linguistic variables and identifies underlying principles of functional variation by looking at how individual linguistic variables co-occur in texts. There are 4 steps to the process: 1) Identification of relevant variables, 2) Extraction of factors from multiple variables, 3) Functional interpretations of factors as dimensions, and 4) Placement of registers on the dimensions.
<strong>Factor analysis</strong> is a complex mathematical procedure that reduces a large number of linguistic variables to a small number of factors, each combining multiple linguistic variables.
<strong>Factor  </strong> is a group of related linguistic variables summarizing a more general tendency (underlying dimension) in the data.
<strong>Scree plot</strong> is a graph which provides an indication of how many factors we should extract. It displays the number of factors (each represented by a small triangle) on the x-axis and eigenvalues on the y-axis.
<strong>Eigenvalue</strong> is a measure of how much variation in the data a factor explains- the larger the value the better.
<strong>One-way ANOVA</strong> is a computational test for statistical significance when we have more than two groups of speakers. It has the following assumptions: 1) independence of observations, 2) normality and 3) homoscedasticity.
<strong>Style</strong> is defined by Coupland (2007: 2) as 'ways of speaking that are indexically linked to social groups, times and places'. It is a unifying notion linking sociolinguistics (social style), stylistics (literary style) and forensic linguistics (individual style).
<strong>Labovian sociolinguistic variable</strong> is defined as 'different ways of saying the same thing' (Labov 2010: 368).
<strong>Circumscribe the variable context</strong> means to define the envelope of variation (lexico-grammatical frame).
<strong>Welch's independent samples t-test</strong> compares two groups of speakers. The t-test compares the mean values of the linguistic variable and takes into consideration the internal variation in each group expressed as variance.
<strong>Variance</strong> is the sum of squared distances of individual values from the group mean divided by the degrees of freedom. It is the squared version of sample standard deviation.
<strong>Degrees of freedom</strong> signifies a number of independent components in a calculation- i.e. components that are not predictable from the previous components. In practice, it is the number of cases or groups minus 1.
<strong>Homoscedasticity</strong> is a technical term for the equality of variances, i.e. the amount of variation in two groups we want to compare.
<strong>Cohen's d</strong> is an effect size measure which is calculated as the difference between the two means expressed in standard deviation units.
<strong>The grand mean</strong> is the mean for the whole corpus.
<strong>Post-hoc tests</strong> are pair-wise comparisons of individual group tests with a correction for multiple testing.
<strong>Non-parametric counterparts</strong> are those with which we do not need to know any information about the parameters (such as the mean of standard deviation) of the variable of interest in the population (Dodge 2008).
<strong>Mann-Whitney U test</strong> is a non-parametric test in which two U values are calculated, one for each group, from which the smaller value is then taken. (Mann & Whitney 1947; Kerby 2014)
<strong>Kruskal-Wallis test</strong> is also a non-parametric test which works on a similar principle but takes into account ranks in multiple groups. (Kruskal & Wallis 1952)
<strong>Rank biserial correlation</strong> can supplement the Mann-Whitney U test and is calculated by subtracting the second rank mean group from the first and dividing by the number of cases. It can take on the values -1 to 1 and the larger the value in absolute terms, the stronger the correlation.
<strong>Repeated measures tests</strong> match individual speakers across conditions and do not assume random distribution of speakers in different groups.
<strong>Multi-way ANOVA (factorial ANOVA)</strong> is a test that takes into account two or more explanatory variables at the same time as well as their interactions.
<strong>Correspondence analysis</strong> is also known as optimal scaling and homogeneity analysis. It is a summary technique which outputs a correspondence plot.
<strong>Correspondence plot</strong> is a visual depiction of a cross-tabulation table which is projected in a (typically) two-dimensional space using the chi-squared distance as a measure of closeness/remoteness of the categories listed in the table.
<strong>Profiles</strong> are proportions (percentages) based on row and column totals. They are expressed as decimal numbers.
<strong>Chi-squared distance</strong> is a weighted form of the Euclidean distance giving proportionally more weight to categories with fewer instances.
<strong>Principle of accountability</strong> states that for the analysis to be meaningful, we have to find all contexts in which all variants of a sociolinguistic variable occur and include them in our analysis.
<strong>External factors</strong> are contextual/situational variables such as a speaker’s age or gender.
<strong>Fixed effects</strong> are explanatory variables that are the direct object of the sociolinguistic investigation.
<strong>Random effects</strong> represent other sources of variation that need to be taken into account, such as individual speaker preferences, but are not part of the research question.
<strong>Diachronic or longitudinal study</strong> is a study which involves time as a variable.
<strong>Diachronic corpora</strong> sample different stages of language or discourse development across time.
<strong>Diachronic representativeness </strong> is a characteristic of a historical corpus which allows it to systematically reflect the population (language use) over time.
<strong>Diachronic polysemy</strong> is a phenomenon where the same linguistic form often changes meaning over time.
<strong>Line graph</strong> is a simple display which plots the time variable on the x-axis and the frequencies of linguistic variables on the y-axis.
<strong>Sparkline</strong> is a small graph the size of a single word that can be seamlessly incorporated into text. They are generally most useful for diachronic data.
<strong>Candlestick plot</strong> is a type of data visualization, where the development of a linguistic variable is summarized as a box and 'wicks' resembling a candlestick. It is often used in financial reports.
<strong>Percentage increase/decrease</strong> is a statistic that indicates how many percentage points the value of a particular linguistic variable increased or decreased between two time periods.
<strong>Bootstrapping</strong> is a process of multiple resampling, which often happens thousands of times, with replacement of the data.
<strong>Bootstrap test</strong> is a non-parametric test of statistical significance which compares two corpora and computes the p-value associated with the comparison.
<strong>Variability-based neighbour clustering (VNC)</strong> computes similarity only between temporally adjacent data points (e.g. individual years that follow each other) and then merges those that are most similar.
<strong>Peaks and troughs</strong> is a method of analysing and visualizing diachronic data, which applies a non-linear regression model (specifically GAM) to data points that show the development of a linguistic variable over time in order to identify statistically significant outliers.
<strong>Meaning Fluctuation Analysis (MFA)</strong> is an extension of the peaks and troughs technique which investigates the development of the meaning of a particular word through analysing a changing profile of collocates around the word.
<strong>Replication</strong> is the process of repeating a study with the same research question but a different dataset.
<strong>Meta-analysis</strong> is a quantitative procedure of statistical synthesis of research results, which is based on combining the effects reported in multiple individual studies and calculating the summary effect (Borenstein 2009).
<strong>Publication bias</strong> is the phenomenon of overreporting stronger, statistically significant results and underreporting null results in published work.
<strong>Null results</strong> are statistically non-significant results.
<strong>Forest plot</strong> provides a summary of a meta-analysis by displaying the effect sizes of individual studies (filled squares), their confidence intervals (whiskers) and the overall effect size (diamond). The size of the square represents the weight of an individual study in the analysis.
<strong>Probability of superiority (PS)</strong> is the probability that a speaker/text picked randomly from the subcorpus with a larger mean value of the target variable will have a higher score than a speaker/text picked from the subcorpus with a lower mean value."""

regex = re.compile(r"<strong>(.*)<\/strong>(.*)")
akaRegex = re.compile(r"(.*)\((.*)\)")
termsDir = os.path.join(os.path.dirname(__file__), 'terms')
termFiles = os.listdir(termsDir)

for defin in definitions.split("\n"):
    dr = regex.match(defin)
    word = dr.group(1)
    aka = akaRegex.match(word)
    if aka != None:
        word = aka.group(1)
        aka = aka.group(2)
    word = word.strip()
    definition = dr.group(2).strip()
    if definition.startswith("is also "):
        definition = definition[7:]
    elif definition.startswith("is a "):
        definition = definition[4:]
    elif definition.startswith("is an "):
        definition = definition[5:]
    definition = definition.strip()
    definition = definition[0].upper() + definition[1:]
    filename = word.lower().replace(" ", "-").replace("/","_").replace("(","").replace(")","").replace("'","")+".json"
    i = 0
    while filename in termFiles:
        filename = word.lower().replace(" ", "-").replace("/","_").replace("(","").replace(")","").replace("'","")+str(i)+".json"
        i+=1
    termFiles.append(filename)
    newObj = {
      "@context": "http://schema.org/",
      "@type": "DefinedTerm",
      "identifier": "https://jackdunncodes.github.io/statsdefinitions/terms/"+filename,
      "name": word,
      "disambiguatingDescription": definition.split(".")[0]+".",
      "description": definition
    }
    if aka != None: newObj["alternateName"] = aka
    newObj = json.dumps(newObj, indent=2)
    with open(os.path.join(termsDir, filename), "w", encoding="utf8") as f:
        f.write(newObj)