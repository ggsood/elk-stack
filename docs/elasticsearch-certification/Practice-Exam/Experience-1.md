The day before the 2018 Elastic China Developers Conference, I took the Elastic Certified Engineer Exam, and made a quick sharing in the lightning speech part of the conference the next day. Yesterday the results of the exam came down. Unfortunately, I failed to pass. However, this time I have a lot of reference experience, and it is worth writing a special article to summarize, to help students who are preparing for the examination and certification to avoid detours.

Examination Content
There is an official outline of Objectives that the exam requires to achieve , which covers a wide range of knowledge points. It is recommended that each point should be practiced according to the document operation. I scanned the outline a few days before the exam, and I felt that I was basically familiar with it, and I didn't practice it carefully. By the time of the exam, I discovered that a few knowledge points were only superficial understanding, the details were not familiar, and there was not enough time to read the documents temporarily.

Exam environment
Use your own computer to log in to the exam website and have a remote desktop connected to the exam virtual machine. There are 5 ES clusters on the virtual machine with different numbers of nodes. The desktop provides a browser that can access kibana and official documentation sites, and a terminal that can ssh to each node of the cluster. All the operations of the exam are basically completed in kibana's sense and this terminal. During this period, only official documents are allowed to be accessed, and solutions are not allowed to be found through Google. We are on-site exams and manual proctoring. Regular exams are remotely proctored via a camera, and a plug-in is required to check background processes. According to regulations, your own machine can only open a browser, and it is not allowed to open other auxiliary tools such as evernotes. The speed of the remote desktop is not very fast. Looking through the document in the browser will feel a bit stuck, so it is required to be very familiar with the document, and it will be accurate when you check it, otherwise it will consume a lot of time to turn pages back and forth. It’s better to use a mouse. It’s much easier to turn pages. I didn’t bring a mouse. It was very painful to use the MAC touchpad to turn pages. In addition, students who use Mac should adapt to copy and paste shortcuts. The test machine copy and paste uses ctrl-c / ctrl-v. If you are used to Mac shortcuts, you will be a little uncomfortable.

Test duration
You can go to the toilet during 3 hours, but it is recommended to drink less water before the test and go to a good toilet because time is precious.

Question format
The 12 test questions are all computer-based questions, each of which describes a scenario and requires solving a problem or achieving a certain goal. Each question will involve 2-3 knowledge points in the exam syllabus, so it is very important to understand the details of each knowledge point. As long as a knowledge point is vaguely understood, it is easy to get stuck. The order of the questions can be controlled by yourself. It is best to familiarize yourself with it first, and do it first if you can get it done immediately. If it takes more than 10 minutes to be unsure, let it go and do it last. I only completed 9 of these 12 questions, and 3 of them were stuck on the spot for a long time because I gave up because of insufficient time. The next part will do a more detailed analysis.

Summary of Types of Exam Questions
1. For a cluster whose status is red, make the cluster green without losing data.
This question I encountered had 3 problems to be solved:

One node is down, find the down node, ssh up, and manually start it;
At this time, the cluster becomes yellow, and there are still shards that cannot be allocated. Check that there is an index in the routings setting. In routing -> include, rack1 is written as rakc1. If it is written incorrectly, please correct it
There are still shards in the cluster that are unassigned. Continue to check and find that there is an index in the routings, and the number of included racks is not enough, causing some replicas to be unassigned. Update routing and let him include more racks. The cluster status changes to green.
The knowledge points examined in this question include how to view the cluster status, how to use the allocation explain api if you view the node list, and how to control the distribution of shards through the allocation routing of the index. Because there are many clustering problems in normal work, this problem is relatively easy to complete.

2. There is a document with similar content dog & cat. It is required to index this document and use match_phrasequery, query dog & cator dog and catmatch.

I didn't come up with this question on the spot. At that time, the first reaction was that the standard tokenizer has been &stripped off, so just use the stop words filter to and strip it off. After the result is configured, it is found that the match fails. Think about it carefully, the match_phase needs to match the position, which &is stripped in the tokenize phase, and stripped in the and token filter phase, so the position is wrong . Use the analyzer api analysis, the location is indeed wrong. Then I thought that the synonym token filter should be used for processing, but the configuration still has problems. At this time, it took too much time, so I just gave up. After I came back, I rehearsed this question and found that it is okay to use the synonym token filter, but the tokenizer should be changed to whitespace, otherwise the & will be stripped off. To sum up, this is usually used less and unskilled, so the time is tight during the exam and my mind is not turned around.

3. Index_a contains some documents, it is required to create index index_b, and index_a documents to index_b through reindex api. It is required to add an integer field, value is the character length of field_x of index_a; add an array type field, value is the word set of field_y. (field_y is a group of words separated by spaces, for example "foo bar", after indexing to index_b, the requirement becomes ["foo", "bar"].

There is no trick in this question, just to examine the use of reindex api + painless script. But I usually don't use painless much. Although in principle I know that one field needs to be size and one needs to be split, but the specific syntax is unfamiliar, and I don't have time to look through the document and give up.

4. Create an index template as required, and index some documents through bulk api to achieve the effect of automatically creating an index. The settings and mappings of the created index should meet the requirements.

This question is relatively simple, familiar with the index template syntax, commonly used settings, mappings settings are OK.

5. Write a query as required, one of the conditions is that a certain keyword must be contained in at least 2 of the 4 fields.

There are no skills in this question, check bool query and minimum_should_match, and you can write it if you are familiar with it

6. Write a search template as required

Familiar with the mustache template language of search template, you can easily write it, but unfortunately, I have never used search template. Although I know the general idea, when I wrote it, I didn't know where there was a grammatical problem. PUT template was always unsuccessful. Guess which position of the character is not translated to produce illegal json characters, or which level of nesting is problematic. In short, the debugging was unsuccessful and a lot of time was wasted.

7. Multi-level nested aggregation, which also includes bucket filtering

No skills, just be familiar with aggregation, aggregation nesting, buckets filtering.

8.  Given a json document, it is required to create an index, define a nested field, index the json document into a nested type, and complete the specified nested query and sort at the same time.

Relatively simple, familiar with the nested type and nested query can be completed.

9.  Given two clusters, both contain an index. It is required to configure cross cluster search to be able to perform cross-cluster search from one of the clusters and write out the search url and query body.

A trap was set in the middle, and a node of the cluster was down and could not be accessed. So we must first solve the problem of node hanging, and then configure the cross cluster in the cluster to execute the query. After confirming that the link is ok, just write the query.

10. There is a 3-node cluster and a kibana. The es cluster does not install x-pack, but the installation package has been placed on the machine, kibana has x-pack installed and security is enabled, so the cluster cannot be connected at this time. It is required to configure security for 3 nodes and set specific passwords for several built-in users. Then add the specified new user, the specified role, and assign role a, role b to the user.

This question can be familiar with x-pack security. First ssh to 3 nodes respectively, and start the nodes after installing x-pack. After the node is successfully connected, use the script that initializes the built-in user password to set the passwords as required. Then you can log in to kibana with elastic, the built-in administrator account. Then through kibana's user and role management interface, add the corresponding users and roles respectively.

There are two questions that I don’t remember. It should be required to create an index and reindex data according to the requirements, and then perform a certain type of query or aggregation. It is relatively simple.

To sum up, this exam is to examine a lot of knowledge points. Although there are only 12 test questions, each test question is a comprehensive investigation of multiple knowledge points. It is not enough for the understanding of ES to stay in theory. The requirements are compared. Strong practical ability. The students who can pass the exam must have rich practical experience. I think the gold content of the certification is still very, very high!