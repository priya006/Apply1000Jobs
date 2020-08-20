from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os  # to get the resume file
import time  # to sleep
import getlinks

# sample application links if we don't want to run get_links.py
# URL_g1 =    'https://jobs.lever.co/amobee/f0bca12a-c0ab-4d44-b62c-df1e74cc04c0/apply?lever-source=Glassdoor'
# URL_l2	=	'https://boards.greenhouse.io/cdbaby/jobs/4030259003?gh_src=6aa9332a3'
# URL_l3	=	'https://jobs.lever.co/u/a399cbcd-e392-4e7e-a1a6-5f880406ab93/apply?lever-source=Glassdoor'
# URL_l4	=	'https://www.natera.com/careers/job-openings?gnk=job&gni=8a7885ac72e8b12a017314be72c01cfa'
# URL_l5	=	'https://www.natera.com/careers/job-openings?gnk=job&gni=8a7885ac72e8b12a017314be72c01cfa'
# URL_l6	=	'https://www.natera.com/careers/job-openings?gnk=job&gni=8a7885ac72e8b12a017314be72c01cfa'
# URL_l7	=	'https://dh.wd3.myworkdayjobs.com/en-US/DHC/job/Portland/Software-Engineer_REQ0520_0015276'
# URL_l8	=	'https://dh.wd3.myworkdayjobs.com/en-US/DHC/job/Portland/Software-Engineer_REQ0520_0015276'
# URL_l9	=	'https://dh.wd3.myworkdayjobs.com/en-US/DHC/job/Portland/Software-Engineer_REQ0520_0015276'
# URL_l10	=	'https://jobs.lever.co/u/a399cbcd-e392-4e7e-a1a6-5f880406ab93/apply?lever-source=Glassdoor'
# URL_l11	=	'https://jobs.lever.co/u/a399cbcd-e392-4e7e-a1a6-5f880406ab93/apply?lever-source=Glassdoor'
# URL_l12	=	'https://jobs.lever.co/token/4a631bdb-fa4d-4d13-9767-94fe4dc001aa/apply?lever-source=Glassdoor'
# URL_l13	=	'https://jobs.lever.co/token/4a631bdb-fa4d-4d13-9767-94fe4dc001aa/apply?lever-source=Glassdoor'
# URL_l14	=	'https://jobs.lever.co/token/4a631bdb-fa4d-4d13-9767-94fe4dc001aa/apply?lever-source=Glassdoor'
# URL_l15	=	'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181/apply'
# URL_l16	=	'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181/apply'
# URL_l17	=	'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181/apply'
# URL_l18	=	'https://jobs.lever.co/matchgroup/ac1355b1-f4c3-4f93-96db-f6f0e1b06b06'
# URL_l19	=	'https://jobs.lever.co/matchgroup/ac1355b1-f4c3-4f93-96db-f6f0e1b06b06'
# URL_l20	=	'https://jobs.lever.co/matchgroup/ac1355b1-f4c3-4f93-96db-f6f0e1b06b06'
# URL_l21	=	'https://instacart.careers/job/?gh_jid=2008462&gh_src=a2c017f81'
# URL_l22	=	'https://instacart.careers/job/?gh_jid=2008462&gh_src=a2c017f81'
# URL_l23	=	'https://instacart.careers/job/?gh_jid=2008462&gh_src=a2c017f81'
# URL_l24	=	'https://boards.greenhouse.io/collectivehealth/jobs/2183536?gh_src=e03993661us'
# URL_l25	=	'https://boards.greenhouse.io/collectivehealth/jobs/2183536?gh_src=e03993661us'
# URL_l26	=	'https://boards.greenhouse.io/collectivehealth/jobs/2183536?gh_src=e03993661us'
# URL_l27	=	'https://jobs.lever.co/afterpaytouch/de68a0d5-a2a2-49ad-b4fc-85d3c3564e9a'
# URL_l28	=	'https://jobs.lever.co/afterpaytouch/de68a0d5-a2a2-49ad-b4fc-85d3c3564e9a'
# URL_l29	=	'https://jobs.lever.co/afterpaytouch/de68a0d5-a2a2-49ad-b4fc-85d3c3564e9a'
# URL_l30	=	'https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/San-Francisco-CA-USA/Sr-Software-Engineer_20WD42558-1'
# URL_l31	=	'https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/San-Francisco-CA-USA/Sr-Software-Engineer_20WD42558-1'
# URL_l32	=	'https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/San-Francisco-CA-USA/Sr-Software-Engineer_20WD42558-1'
# URL_l33	=	'https://jobs.lever.co/caffeine/464c6fac-ecef-45f0-9240-da7ad5e76add'
# URL_l34	=	'https://jobs.lever.co/caffeine/464c6fac-ecef-45f0-9240-da7ad5e76add'
# URL_l35	=	'https://jobs.lever.co/caffeine/464c6fac-ecef-45f0-9240-da7ad5e76add'
# URL_l36	=	'https://careers-nevro.icims.com/jobs/2880/software-development-engineer/job?ss=1'
# URL_l37	=	'https://careers-nevro.icims.com/jobs/2880/software-development-engineer/job?ss=1'
# URL_l38	=	'https://careers-nevro.icims.com/jobs/2880/software-development-engineer/job?ss=1'
# URL_l39	=	'https://www.perfectworld.com/careers/1523#-1198548516'
# URL_l40	=	'https://www.perfectworld.com/careers/1523#-1198548516'
# URL_l41	=	'https://www.perfectworld.com/careers/1523#-1198548516'
# URL_l42	=	'https://jobs.lever.co/qbio/cd89de49-934e-4a8d-a6ea-7cc618307edc/apply?lever-source=Glassdoor'
# URL_l43	=	'https://jobs.lever.co/qbio/cd89de49-934e-4a8d-a6ea-7cc618307edc/apply?lever-source=Glassdoor'
# URL_l44	=	'https://jobs.lever.co/qbio/cd89de49-934e-4a8d-a6ea-7cc618307edc/apply?lever-source=Glassdoor'
# URL_l45	=	'https://www.benchling.com/careers/?gh_jid=172257&gh_src=wq143b'
# URL_l46	=	'https://www.benchling.com/careers/?gh_jid=172257&gh_src=wq143b'
# URL_l47	=	'https://www.benchling.com/careers/?gh_jid=172257&gh_src=wq143b'
# URL_l48	=	'https://jobs.lever.co/outlier/cf0b9875-61b1-45cb-88cc-c96638baf71e/apply?lever-source=Glassdoor'
# URL_l49	=	'https://jobs.lever.co/outlier/cf0b9875-61b1-45cb-88cc-c96638baf71e/apply?lever-source=Glassdoor'
# URL_l50	=	'https://jobs.lever.co/outlier/cf0b9875-61b1-45cb-88cc-c96638baf71e/apply?lever-source=Glassdoor'
# URL_l51	=	'https://jobs.lever.co/trueaccord/c29e4304-d55a-42c2-99bc-eb9e0a4adee1/apply?lever-source=Glassdoor'
# URL_l52	=	'https://jobs.lever.co/trueaccord/c29e4304-d55a-42c2-99bc-eb9e0a4adee1/apply?lever-source=Glassdoor'
# URL_l53	=	'https://jobs.lever.co/trueaccord/c29e4304-d55a-42c2-99bc-eb9e0a4adee1/apply?lever-source=Glassdoor'
# URL_l54	=	'https://jobs.lever.co/zeplin/22c36b56-be1e-4a67-8757-2615928b6fa5/apply?lever-source=Glassdoor'
# URL_l55	=	'https://jobs.lever.co/zeplin/22c36b56-be1e-4a67-8757-2615928b6fa5/apply?lever-source=Glassdoor'
# URL_l56	=	'https://jobs.lever.co/zeplin/22c36b56-be1e-4a67-8757-2615928b6fa5/apply?lever-source=Glassdoor'
# URL_l57	=	'https://careers.twitter.com/en/work-for-twitter/202008/50840064-e199-4879-abe5-bd0fcd628939/caf3fd59-cd9b-408c-bf69-4546b9208976.html/staff-software-engineer-backend-tweet-services.html'
# URL_l58	=	'https://jobs.smartrecruiters.com/TurnitinLLC/743999712937661-software-engineer-growth-ruby-on-rails-'
# URL_l59	=	'https://jobs.smartrecruiters.com/TurnitinLLC/743999712937661-software-engineer-growth-ruby-on-rails-'
# URL_l60	=	'https://jobs.smartrecruiters.com/TurnitinLLC/743999712937661-software-engineer-growth-ruby-on-rails-'
# URL_l61	=	'https://jobs.lever.co/token/4a631bdb-fa4d-4d13-9767-94fe4dc001aa/apply?lever-source=Glassdoor'
# URL_l62	=	'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181/apply'
# URL_l63	=	'https://jobs.lever.co/matchgroup/ac1355b1-f4c3-4f93-96db-f6f0e1b06b06'
# URL_l64	=	'https://instacart.careers/job/?gh_jid=2008462&gh_src=a2c017f81'
# URL_l65	=	'https://boards.greenhouse.io/collectivehealth/jobs/2183536?gh_src=e03993661us'
# URL_l66	=	'https://jobs.lever.co/afterpaytouch/de68a0d5-a2a2-49ad-b4fc-85d3c3564e9a'
# URL_l67	=	'https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/San-Francisco-CA-USA/Sr-Software-Engineer_20WD42558-1'
# URL_l68	=	'https://jobs.lever.co/caffeine/464c6fac-ecef-45f0-9240-da7ad5e76add'
# URL_l69	=	'https://careers-nevro.icims.com/jobs/2880/software-development-engineer/job?ss=1'
# URL_l70	=	'https://www.perfectworld.com/careers/1523#-1198548516'
# URL_l71	=	'https://jobs.lever.co/qbio/cd89de49-934e-4a8d-a6ea-7cc618307edc/apply?lever-source=Glassdoor'
# URL_l72	=	'https://www.benchling.com/careers/?gh_jid=172257&gh_src=wq143b'
# URL_l73	=	'https://jobs.lever.co/outlier/cf0b9875-61b1-45cb-88cc-c96638baf71e/apply?lever-source=Glassdoor'
# URL_l74	=	'https://jobs.lever.co/trueaccord/c29e4304-d55a-42c2-99bc-eb9e0a4adee1/apply?lever-source=Glassdoor'
# URL_l75	=	'https://jobs.lever.co/zeplin/22c36b56-be1e-4a67-8757-2615928b6fa5/apply?lever-source=Glassdoor'
# URL_l76	=	'https://jobs.smartrecruiters.com/TurnitinLLC/743999712937661-software-engineer-growth-ruby-on-rails-'
# URL_l77	=	'https://careers.twitter.com/en/work-for-twitter/202008/440f814b-a814-407e-9dae-78bbe53b99e1/9adea616-15c6-40c5-838f-4e5a7f8211ad.html/software-engineer-data-health-data-engineering.html'
# URL_l78	=	'https://boards.greenhouse.io/c3iot/jobs/4227502002?gh_src=310ebbdf2'
# URL_l79	=	'https://boards.greenhouse.io/c3iot/jobs/4227502002?gh_src=310ebbdf2'
# URL_l80	=	'https://boards.greenhouse.io/c3iot/jobs/4227502002?gh_src=310ebbdf2'
# URL_l81	=	'https://jobs.smartrecruiters.com/TurnitinLLC/743999712937661-software-engineer-growth-ruby-on-rails-'
# URL_l82	=	'https://jobs.smartrecruiters.com/TurnitinLLC/743999712937661-software-engineer-growth-ruby-on-rails-'
# URL_l83	=	'https://jobs.smartrecruiters.com/TurnitinLLC/743999712937661-software-engineer-growth-ruby-on-rails-'
# URL_l84	=	'https://boards.greenhouse.io/translationunitedmastersstashed'
# URL_l85	=	'https://boards.greenhouse.io/translationunitedmastersstashed'
# URL_l86	=	'https://boards.greenhouse.io/translationunitedmastersstashed'
# URL_l87	=	'https://jobs.smartrecruiters.com/Renaissance/743999717254437-senior-software-engineer-full-stack-schoolzilla-remote-us-'
# URL_l88	=	'https://jobs.smartrecruiters.com/Renaissance/743999717254437-senior-software-engineer-full-stack-schoolzilla-remote-us-'
# URL_l89	=	'https://jobs.smartrecruiters.com/Renaissance/743999717254437-senior-software-engineer-full-stack-schoolzilla-remote-us-'
# URL_l90	=	'https://jobs.lever.co/zeplin/b4a1eba0-148b-4450-8432-52dcf6a9225d/apply?lever-source=Glassdoor'
# URL_l91	=	'https://jobs.lever.co/zeplin/b4a1eba0-148b-4450-8432-52dcf6a9225d/apply?lever-source=Glassdoor'
# URL_l92	=	'https://jobs.lever.co/zeplin/b4a1eba0-148b-4450-8432-52dcf6a9225d/apply?lever-source=Glassdoor'
# URL_l93	=	'https://www.ixl.com/company/careers?gh_jid=4825617002&gh_src=9d5a2c6f2us'
# URL_l94	=	'https://www.ixl.com/company/careers?gh_jid=4825617002&gh_src=9d5a2c6f2us'
# URL_l95	=	'https://www.ixl.com/company/careers?gh_jid=4825617002&gh_src=9d5a2c6f2us'
# URL_l96	=	'https://jobs.lever.co/amobee/f0bca12a-c0ab-4d44-b62c-df1e74cc04c0/apply?lever-source=Glassdoor'
# URL_l97	=	'https://jobs.lever.co/amobee/f0bca12a-c0ab-4d44-b62c-df1e74cc04c0/apply?lever-source=Glassdoor'
# URL_l98	=	'https://jobs.lever.co/amobee/f0bca12a-c0ab-4d44-b62c-df1e74cc04c0/apply?lever-source=Glassdoor'
# URL_l99	=	'https://recruiting.ultipro.com/RUB1004RUGH/JobBoard/b65b7a3c-d3fb-4185-85d4-ac59fac2f527/OpportunityDetail?opportunityId=aeb63086-4a2b-4d75-8a40-c1894c52bb05'
# URL_l100	=	'https://recruiting.ultipro.com/RUB1004RUGH/JobBoard/b65b7a3c-d3fb-4185-85d4-ac59fac2f527/OpportunityDetail?opportunityId=aeb63086-4a2b-4d75-8a40-c1894c52bb05'
# URL_l101	=	'https://recruiting.ultipro.com/RUB1004RUGH/JobBoard/b65b7a3c-d3fb-4185-85d4-ac59fac2f527/OpportunityDetail?opportunityId=aeb63086-4a2b-4d75-8a40-c1894c52bb05'
# URL_l102	=	'https://boards.greenhouse.io/postmates/jobs/1486672?gh_src=13c224d11'
# URL_l103	=	'https://boards.greenhouse.io/postmates/jobs/1486672?gh_src=13c224d11'
# URL_l104	=	'https://boards.greenhouse.io/postmates/jobs/1486672?gh_src=13c224d11'
# URL_l105	=	'https://jobs.lever.co/pmdsoft/d7b29a85-e567-4177-a9d6-07954108cf47'
# URL_l106	=	'https://jobs.lever.co/pmdsoft/d7b29a85-e567-4177-a9d6-07954108cf47'
# URL_l107	=	'https://jobs.lever.co/pmdsoft/d7b29a85-e567-4177-a9d6-07954108cf47'
# URL_l108	=	'https://boards.greenhouse.io/c3iot/jobs/4056116002?gh_src=37d81d322'
# URL_l109	=	'https://boards.greenhouse.io/c3iot/jobs/4056116002?gh_src=37d81d322'
# URL_l110	=	'https://boards.greenhouse.io/c3iot/jobs/4056116002?gh_src=37d81d322'
# URL_l111	=	'https://boards.greenhouse.io/c3iot/jobs/4227502002?gh_src=310ebbdf2'
# URL_l112	=	'https://jobs.smartrecruiters.com/TurnitinLLC/743999712937661-software-engineer-growth-ruby-on-rails-'
# URL_l113	=	'https://boards.greenhouse.io/translationunitedmastersstashed'
# URL_l114	=	'https://jobs.smartrecruiters.com/Renaissance/743999717254437-senior-software-engineer-full-stack-schoolzilla-remote-us-'
# URL_l115	=	'https://jobs.lever.co/zeplin/b4a1eba0-148b-4450-8432-52dcf6a9225d/apply?lever-source=Glassdoor'
# URL_l116	=	'https://www.ixl.com/company/careers?gh_jid=4825617002&gh_src=9d5a2c6f2us'
# URL_l117	=	'https://jobs.lever.co/amobee/f0bca12a-c0ab-4d44-b62c-df1e74cc04c0/apply?lever-source=Glassdoor'
# URL_l118	=	'https://recruiting.ultipro.com/RUB1004RUGH/JobBoard/b65b7a3c-d3fb-4185-85d4-ac59fac2f527/OpportunityDetail?opportunityId=aeb63086-4a2b-4d75-8a40-c1894c52bb05'
# URL_l119	=	'https://boards.greenhouse.io/postmates/jobs/1486672?gh_src=13c224d11'
# URL_l120	=	'https://jobs.lever.co/pmdsoft/d7b29a85-e567-4177-a9d6-07954108cf47'
# URL_l121	=	'https://boards.greenhouse.io/c3iot/jobs/4056116002?gh_src=37d81d322'
# URL_l122	=	'https://boards.greenhouse.io/affirm/jobs/4126463003?gh_src=d2d050343us'
# URL_l123	=	'https://boards.greenhouse.io/affirm/jobs/4126463003?gh_src=d2d050343us'
# URL_l124	=	'https://boards.greenhouse.io/affirm/jobs/4126463003?gh_src=d2d050343us'
# URL_l125	=	'https://jobs.lever.co/quizlet-2/bf9d612b-8759-439e-b8d6-c26cb4ff2a2b/apply?lever-source=Glassdoor'
# URL_l126	=	'https://jobs.lever.co/quizlet-2/bf9d612b-8759-439e-b8d6-c26cb4ff2a2b/apply?lever-source=Glassdoor'
# URL_l127	=	'https://jobs.lever.co/quizlet-2/bf9d612b-8759-439e-b8d6-c26cb4ff2a2b/apply?lever-source=Glassdoor'
# URL_l128	=	'https://careers.twitter.com/en/work-for-twitter/202008/4bc79b47-96c9-4010-92b4-3d47e865dcc8/7d8ddbf6-5d2d-41af-baf2-4c565390bdbd.html/staff-software-engineer-onboarding.html'
# URL_l129	=	'https://careers.twitter.com/en/work-for-twitter/202008/4bc79b47-96c9-4010-92b4-3d47e865dcc8/7d8ddbf6-5d2d-41af-baf2-4c565390bdbd.html/staff-software-engineer-onboarding.html'
# URL_l130	=	'https://waymo.com/joinus/2077358?gh_jid=2077358&gh_src=0d04abc21'
# URL_l131	=	'https://waymo.com/joinus/2077358?gh_jid=2077358&gh_src=0d04abc21'
# URL_l132	=	'https://waymo.com/joinus/2077358?gh_jid=2077358&gh_src=0d04abc21'
# URL_l133	=	'https://jobs.lever.co/kiddom/c45db39d-db8d-444d-8540-5ee9455f472a'
# URL_l134	=	'https://jobs.lever.co/kiddom/c45db39d-db8d-444d-8540-5ee9455f472a'
# URL_l135	=	'https://jobs.lever.co/kiddom/c45db39d-db8d-444d-8540-5ee9455f472a'
# URL_l136	=	'https://apply.workable.com/smartnews/j/EC7D988063'
# URL_l137	=	'https://apply.workable.com/smartnews/j/EC7D988063'
# URL_l138	=	'https://apply.workable.com/smartnews/j/EC7D988063'
# URL_l139	=	'https://jobs.lever.co/bolt/5a260836-617b-47c4-a4d5-51fd012070d8/apply?lever-source=Glassdoor'
# URL_l140	=	'https://jobs.lever.co/bolt/5a260836-617b-47c4-a4d5-51fd012070d8/apply?lever-source=Glassdoor'
# URL_l141	=	'https://jobs.lever.co/bolt/5a260836-617b-47c4-a4d5-51fd012070d8/apply?lever-source=Glassdoor'
# URL_l142	=	'https://boards.greenhouse.io/formation/jobs/2265465?gh_src=a8d29cc11us'
# URL_l143	=	'https://boards.greenhouse.io/formation/jobs/2265465?gh_src=a8d29cc11us'
# URL_l144	=	'https://boards.greenhouse.io/formation/jobs/2265465?gh_src=a8d29cc11us'
# URL_l145	=	'https://apply.workable.com/payjoy/j/6A52726894'
# URL_l146	=	'https://apply.workable.com/payjoy/j/6A52726894'
# URL_l147	=	'https://apply.workable.com/payjoy/j/6A52726894'
# URL_l148	=	'https://jobs.lever.co/bighealth/40256df2-1389-4438-a00d-4be6f0158685'
# URL_l149	=	'https://jobs.lever.co/bighealth/40256df2-1389-4438-a00d-4be6f0158685'
# URL_l150	=	'https://jobs.lever.co/bighealth/40256df2-1389-4438-a00d-4be6f0158685'
# URL_l151	=	'https://boards.greenhouse.io/pocketgems/jobs/1461233?gh_src=985c640e1'
# URL_l152	=	'https://boards.greenhouse.io/pocketgems/jobs/1461233?gh_src=985c640e1'
# URL_l153	=	'https://boards.greenhouse.io/pocketgems/jobs/1461233?gh_src=985c640e1'
# URL_l154	=	'https://jobs.lever.co/varomoney/024d6277-4394-47bd-914b-bd6c3a9de232'
# URL_l155	=	'https://jobs.lever.co/varomoney/024d6277-4394-47bd-914b-bd6c3a9de232'
# URL_l156	=	'https://jobs.lever.co/varomoney/024d6277-4394-47bd-914b-bd6c3a9de232'
# URL_l157	=	'https://jobs.lever.co/aalto/de145c59-07dc-423f-9ba2-e7d45724481a/apply?lever-source=Glassdoor'
# URL_l158	=	'https://jobs.lever.co/aalto/de145c59-07dc-423f-9ba2-e7d45724481a/apply?lever-source=Glassdoor'
# URL_l159	=	'https://jobs.lever.co/aalto/de145c59-07dc-423f-9ba2-e7d45724481a/apply?lever-source=Glassdoor'
# URL_l160	=	'https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/San-Francisco-CA-USA/Software-Engineer-3_19WD36823-1'
# URL_l161	=	'https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/San-Francisco-CA-USA/Software-Engineer-3_19WD36823-1'
# URL_l162	=	'https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/San-Francisco-CA-USA/Software-Engineer-3_19WD36823-1'
# URL_l163	=	'https://jobs.lever.co/alphahealth.com/f94fd703-6ccc-4811-8ce9-4b4b389bddae/apply?lever-source=Glassdoor'
# URL_l164	=	'https://jobs.lever.co/alphahealth.com/f94fd703-6ccc-4811-8ce9-4b4b389bddae/apply?lever-source=Glassdoor'
# URL_l165	=	'https://jobs.lever.co/alphahealth.com/f94fd703-6ccc-4811-8ce9-4b4b389bddae/apply?lever-source=Glassdoor'
# URL_l166	=	'https://jobs.smartrecruiters.com/Wish/743999715141311-software-engineer-web-and-mobile'
# URL_l167	=	'https://jobs.smartrecruiters.com/Wish/743999715141311-software-engineer-web-and-mobile'
# URL_l168	=	'https://jobs.smartrecruiters.com/Wish/743999715141311-software-engineer-web-and-mobile'
# URL_l169	=	'https://jobs.lever.co/flockjay/e7d88237-7873-4b63-82a5-4806c448fced/apply?lever-source=Glassdoor'
# URL_l170	=	'https://jobs.lever.co/flockjay/e7d88237-7873-4b63-82a5-4806c448fced/apply?lever-source=Glassdoor'
# URL_l171	=	'https://jobs.lever.co/flockjay/e7d88237-7873-4b63-82a5-4806c448fced/apply?lever-source=Glassdoor'
# URL_l172	=	'https://jobs.lever.co/goforward/5d00954d-a953-4b10-b9ec-0254e1636f0a/apply?lever-source=Glassdoor'
# URL_l173	=	'https://jobs.lever.co/goforward/5d00954d-a953-4b10-b9ec-0254e1636f0a/apply?lever-source=Glassdoor'
# URL_l174	=	'https://jobs.lever.co/goforward/5d00954d-a953-4b10-b9ec-0254e1636f0a/apply?lever-source=Glassdoor'
# URL_l175	=	'https://alteryx.wd5.myworkdayjobs.com/en-US/AlteryxCareers/job/Redwood-City-California/Senior-Quality-Engineer---Data-Engine_R2541'
# URL_l176	=	'https://alteryx.wd5.myworkdayjobs.com/en-US/AlteryxCareers/job/Redwood-City-California/Senior-Quality-Engineer---Data-Engine_R2541'
# URL_l177	=	'https://alteryx.wd5.myworkdayjobs.com/en-US/AlteryxCareers/job/Redwood-City-California/Senior-Quality-Engineer---Data-Engine_R2541'
# URL_l178	=	'https://boards.greenhouse.io/celonis/jobs/4017268003?gh_src=1c55098d3'
# URL_l179	=	'https://boards.greenhouse.io/celonis/jobs/4017268003?gh_src=1c55098d3'
# URL_l180	=	'https://boards.greenhouse.io/celonis/jobs/4017268003?gh_src=1c55098d3'
# URL_l181	=	'https://boards.greenhouse.io/affirm/jobs/4126463003?gh_src=d2d050343us'
# URL_l182	=	'https://jobs.lever.co/quizlet-2/bf9d612b-8759-439e-b8d6-c26cb4ff2a2b/apply?lever-source=Glassdoor'
# URL_l183	=	'https://careers.twitter.com/en/work-for-twitter/202008/4bc79b47-96c9-4010-92b4-3d47e865dcc8/7d8ddbf6-5d2d-41af-baf2-4c565390bdbd.html/staff-software-engineer-onboarding.html'
# URL_l184	=	'https://waymo.com/joinus/2077358?gh_jid=2077358&gh_src=0d04abc21'
# URL_l185	=	'https://jobs.lever.co/kiddom/c45db39d-db8d-444d-8540-5ee9455f472a'
# URL_l186	=	'https://apply.workable.com/smartnews/j/EC7D988063'
# URL_l187	=	'https://jobs.lever.co/bolt/5a260836-617b-47c4-a4d5-51fd012070d8/apply?lever-source=Glassdoor'
# URL_l188	=	'https://boards.greenhouse.io/formation/jobs/2265465?gh_src=a8d29cc11us'
# URL_l189	=	'https://apply.workable.com/payjoy/j/6A52726894'
# URL_l190	=	'https://jobs.lever.co/bighealth/40256df2-1389-4438-a00d-4be6f0158685'
# URL_l191	=	'https://boards.greenhouse.io/pocketgems/jobs/1461233?gh_src=985c640e1'
# URL_l192	=	'https://jobs.lever.co/varomoney/024d6277-4394-47bd-914b-bd6c3a9de232'
# URL_l193	=	'https://jobs.lever.co/aalto/de145c59-07dc-423f-9ba2-e7d45724481a/apply?lever-source=Glassdoor'
# URL_l194	=	'https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/San-Francisco-CA-USA/Software-Engineer-3_19WD36823-1'
# URL_l195	=	'https://jobs.lever.co/alphahealth.com/f94fd703-6ccc-4811-8ce9-4b4b389bddae/apply?lever-source=Glassdoor'
# URL_l196	=	'https://jobs.smartrecruiters.com/Wish/743999715141311-software-engineer-web-and-mobile'
# URL_l197	=	'https://jobs.lever.co/flockjay/e7d88237-7873-4b63-82a5-4806c448fced/apply?lever-source=Glassdoor'
# URL_l198	=	'https://jobs.lever.co/goforward/5d00954d-a953-4b10-b9ec-0254e1636f0a/apply?lever-source=Glassdoor'
# URL_l199	=	'https://alteryx.wd5.myworkdayjobs.com/en-US/AlteryxCareers/job/Redwood-City-California/Senior-Quality-Engineer---Data-Engine_R2541'
# URL_l200	=	'https://boards.greenhouse.io/celonis/jobs/4017268003?gh_src=1c55098d3'
# URL_l201	=	'https://jobs.lever.co/goforward/aa4ba99a-9450-49ba-a407-668cca8c6928/apply?lever-source=Glassdoor'
# URL_l202	=	'https://jobs.lever.co/goforward/aa4ba99a-9450-49ba-a407-668cca8c6928/apply?lever-source=Glassdoor'
# URL_l203	=	'https://jobs.lever.co/goforward/aa4ba99a-9450-49ba-a407-668cca8c6928/apply?lever-source=Glassdoor'
# URL_l204	=	'https://boards.greenhouse.io/dominodatalab/jobs/2196725?gh_src=1b2bcfef1us'
# URL_l205	=	'https://boards.greenhouse.io/dominodatalab/jobs/2196725?gh_src=1b2bcfef1us'
# URL_l206	=	'https://boards.greenhouse.io/dominodatalab/jobs/2196725?gh_src=1b2bcfef1us'
# URL_l207	=	'https://www.benchling.com/careers/?gh_jid=2272820&gh_src=dabd254e1us'
# URL_l208	=	'https://www.benchling.com/careers/?gh_jid=2272820&gh_src=dabd254e1us'
# URL_l209	=	'https://www.benchling.com/careers/?gh_jid=2272820&gh_src=dabd254e1us'
# URL_l210	=	'https://www.benchling.com/careers/?gh_jid=1515023&gh_src=086767ac1'
# URL_l211	=	'https://www.benchling.com/careers/?gh_jid=1515023&gh_src=086767ac1'
# URL_l212	=	'https://www.benchling.com/careers/?gh_jid=1515023&gh_src=086767ac1'
# URL_l213	=	'https://jobs.lever.co/sideinc/e93d505d-4434-453a-b829-de314dc9b1d8/apply?lever-source=Glassdoor'
# URL_l214	=	'https://jobs.lever.co/sideinc/e93d505d-4434-453a-b829-de314dc9b1d8/apply?lever-source=Glassdoor'
# URL_l215	=	'https://jobs.lever.co/sideinc/e93d505d-4434-453a-b829-de314dc9b1d8/apply?lever-source=Glassdoor'
# URL_l216	=	'https://jobs.cisco.com/jobs/ProjectDetail/AppD-Software-Engineer-Dynamic-Languages/1291691?source=Glassdoor'
# URL_l217	=	'https://jobs.cisco.com/jobs/ProjectDetail/AppD-Software-Engineer-Dynamic-Languages/1291691?source=Glassdoor'
# URL_l218	=	'https://jobs.cisco.com/jobs/ProjectDetail/AppD-Software-Engineer-Dynamic-Languages/1291691?source=Glassdoor'
# URL_l219	=	'https://careers.jobscore.com/careers/tapjoy/jobs/senior-software-engineer-back-end-bAF_RSnT8r6PCkaKkAGGpB?jpid=d890zm34Kr6Q8vaKk9ke5_&name=GlassDoor&sid=69'
# URL_l220	=	'https://careers.jobscore.com/careers/tapjoy/jobs/senior-software-engineer-back-end-bAF_RSnT8r6PCkaKkAGGpB?jpid=d890zm34Kr6Q8vaKk9ke5_&name=GlassDoor&sid=69'
# URL_l221	=	'https://careers.jobscore.com/careers/tapjoy/jobs/senior-software-engineer-back-end-bAF_RSnT8r6PCkaKkAGGpB?jpid=d890zm34Kr6Q8vaKk9ke5_&name=GlassDoor&sid=69'
# URL_l222	=	'https://boards.greenhouse.io/postmates/jobs/1486667?gh_src=7523f7221'
# URL_l223	=	'https://boards.greenhouse.io/postmates/jobs/1486667?gh_src=7523f7221'
# URL_l224	=	'https://boards.greenhouse.io/postmates/jobs/1486667?gh_src=7523f7221'
# URL_l225	=	'https://jobs.lever.co/zeplin/b75431c7-45bb-48cf-8956-5acf584432d8/apply?lever-source=Glassdoor'
# URL_l226	=	'https://jobs.lever.co/zeplin/b75431c7-45bb-48cf-8956-5acf584432d8/apply?lever-source=Glassdoor'
# URL_l227	=	'https://jobs.lever.co/zeplin/b75431c7-45bb-48cf-8956-5acf584432d8/apply?lever-source=Glassdoor'
# URL_l228	=	'https://jobs.smartrecruiters.com/Wish/743999715152412-software-engineer-ads'
# URL_l229	=	'https://jobs.smartrecruiters.com/Wish/743999715152412-software-engineer-ads'
# URL_l230	=	'https://jobs.smartrecruiters.com/Wish/743999715152412-software-engineer-ads'
# URL_l231	=	'https://jobs.lever.co/varomoney/c1626340-61c8-4e98-8e41-f2d16c4e9cf6'
# URL_l232	=	'https://jobs.lever.co/varomoney/c1626340-61c8-4e98-8e41-f2d16c4e9cf6'
# URL_l233	=	'https://jobs.lever.co/varomoney/c1626340-61c8-4e98-8e41-f2d16c4e9cf6'
# URL_l234	=	'https://fhlbsf.wd5.myworkdayjobs.com/en-US/FHLBSF/job/333-Bush-St-Suite-2700/Lead-Software-Engineer--Dir_REQ1149'
# URL_l235	=	'https://fhlbsf.wd5.myworkdayjobs.com/en-US/FHLBSF/job/333-Bush-St-Suite-2700/Lead-Software-Engineer--Dir_REQ1149'
# URL_l236	=	'https://fhlbsf.wd5.myworkdayjobs.com/en-US/FHLBSF/job/333-Bush-St-Suite-2700/Lead-Software-Engineer--Dir_REQ1149'
# URL_l237	=	'https://boards.greenhouse.io/grammarly/jobs/2176972?gh_src=431399a01us'
# URL_l238	=	'https://boards.greenhouse.io/grammarly/jobs/2176972?gh_src=431399a01us'
# URL_l239	=	'https://boards.greenhouse.io/grammarly/jobs/2176972?gh_src=431399a01us'
# URL_l240	=	'https://jobs.lever.co/verkada/b4839b57-0a75-4f72-9e3c-fc5b77809243/apply?lever-source=Glassdoor'
# URL_l241	=	'https://jobs.lever.co/verkada/b4839b57-0a75-4f72-9e3c-fc5b77809243/apply?lever-source=Glassdoor'
# URL_l242	=	'https://jobs.lever.co/verkada/b4839b57-0a75-4f72-9e3c-fc5b77809243/apply?lever-source=Glassdoor'
# URL_l243	=	'https://jobs.lever.co/socotra/f964409b-95d8-4580-ba94-804714e37b3a/apply?lever-source=Glassdoor'
# URL_l244	=	'https://jobs.lever.co/socotra/f964409b-95d8-4580-ba94-804714e37b3a/apply?lever-source=Glassdoor'
# URL_l245	=	'https://jobs.lever.co/socotra/f964409b-95d8-4580-ba94-804714e37b3a/apply?lever-source=Glassdoor'
# URL_l246	=	'https://jobs.lever.co/goforward/aa4ba99a-9450-49ba-a407-668cca8c6928/apply?lever-source=Glassdoor'
# URL_l247	=	'https://boards.greenhouse.io/dominodatalab/jobs/2196725?gh_src=1b2bcfef1us'
# URL_l248	=	'https://www.benchling.com/careers/?gh_jid=2272820&gh_src=dabd254e1us'
# URL_l249	=	'https://www.benchling.com/careers/?gh_jid=1515023&gh_src=086767ac1'
# URL_l250	=	'https://jobs.lever.co/sideinc/e93d505d-4434-453a-b829-de314dc9b1d8/apply?lever-source=Glassdoor'
# URL_l251	=	'https://jobs.cisco.com/jobs/ProjectDetail/AppD-Software-Engineer-Dynamic-Languages/1291691?source=Glassdoor'
# URL_l252	=	'https://careers.jobscore.com/careers/tapjoy/jobs/senior-software-engineer-back-end-bAF_RSnT8r6PCkaKkAGGpB?jpid=d890zm34Kr6Q8vaKk9ke5_&name=GlassDoor&sid=69'
# URL_l253	=	'https://boards.greenhouse.io/postmates/jobs/1486667?gh_src=7523f7221'
# URL_l254	=	'https://jobs.lever.co/zeplin/b75431c7-45bb-48cf-8956-5acf584432d8/apply?lever-source=Glassdoor'
# URL_l255	=	'https://jobs.smartrecruiters.com/Wish/743999715152412-software-engineer-ads'
# URL_l256	=	'https://jobs.lever.co/varomoney/c1626340-61c8-4e98-8e41-f2d16c4e9cf6'
# URL_l257	=	'https://fhlbsf.wd5.myworkdayjobs.com/en-US/FHLBSF/job/333-Bush-St-Suite-2700/Lead-Software-Engineer--Dir_REQ1149'
# URL_l258	=	'https://boards.greenhouse.io/grammarly/jobs/2176972?gh_src=431399a01us'
# URL_l259	=	'https://jobs.lever.co/verkada/b4839b57-0a75-4f72-9e3c-fc5b77809243/apply?lever-source=Glassdoor'
# URL_l260	=	'https://jobs.lever.co/socotra/f964409b-95d8-4580-ba94-804714e37b3a/apply?lever-source=Glassdoor'

# URL_l3 = 'https://jobs.lever.co/fleetsmith/eb6648a6-7ad9-4f4a-9918-8b124e10c525/apply?lever-source=Glassdoor'
# URL_l4 = 'https://jobs.lever.co/stellar/0e5a506b-1964-40b4-93ab-31a1ee4e4f90/apply?lever-source=Glassdoor'
# URL_l6 = 'https://jobs.lever.co/verkada/29c66147-82ef-4293-9a6a-aeed7e6d619e/apply?lever-source=Glassdoor'
# URL_l8 = 'https://jobs.lever.co/rimeto/bdca896f-e7e7-4f27-a894-41b47c729c63/apply?lever-source=Glassdoor'
# URL_l9 = 'https://jobs.lever.co/color/20ea56b8-fed2-413c-982d-6173e336d51c/apply?lever-source=Glassdoor'


# there's probably a prettier way to do all of this
# test URLs so we don't have to call get_links
URL_g1 = 'https://jobs.lever.co/amobee/f0bca12a-c0ab-4d44-b62c-df1e74cc04c0/apply?lever-source=Glassdoor'
URLS = [URL_g1]
# URLS = [URL_g1,URL_l3,	URL_l4,	URL_l5,	URL_l6,	URL_l7,	URL_l8,	URL_l9,	URL_l10,URL_l11,	URL_l12,	URL_l13,	URL_l14,	URL_l15,	URL_l16,	URL_l17,	URL_l18,	URL_l19,	URL_l20,	URL_l21,	URL_l22,	URL_l23,	URL_l24,	URL_l25,	URL_l26,	URL_l27,	URL_l28,	URL_l29,	URL_l30,	URL_l31,	URL_l32,	URL_l33,	URL_l34,	URL_l35,	URL_l36,	URL_l37,	URL_l38,	URL_l39,	URL_l40,	URL_l41,	URL_l42,	URL_l43,	URL_l44,	URL_l45,	URL_l46,	URL_l47,	URL_l48,	URL_l49,	URL_l50,	URL_l51,	URL_l52,	URL_l53,	URL_l54,	URL_l55,	URL_l56,	URL_l57,	URL_l58,	URL_l59,	URL_l60,	URL_l61,	URL_l62,	URL_l63,	URL_l64,	URL_l65,	URL_l66,	URL_l67,	URL_l68,	URL_l69,	URL_l70,	URL_l71,	URL_l72,	URL_l73,	URL_l74,	URL_l75,	URL_l76,	URL_l77,	URL_l78,	URL_l79,	URL_l80,	URL_l81,	URL_l82,	URL_l83,	URL_l84,	URL_l85,	URL_l86,	URL_l87,	URL_l88,	URL_l89,	URL_l90,	URL_l91,	URL_l92,	URL_l93,	URL_l94,	URL_l95,	URL_l96,	URL_l97,	URL_l98,	URL_l99,	URL_l100,	URL_l101,	URL_l102,	URL_l103,	URL_l104,	URL_l105,	URL_l106,	URL_l107,	URL_l108,	URL_l109,	URL_l110,	URL_l111,	URL_l112,	URL_l113,	URL_l114,	URL_l115,	URL_l116,	URL_l117,	URL_l118,	URL_l119,	URL_l120,	URL_l121,	URL_l122,	URL_l123,	URL_l124,	URL_l125,	URL_l126,	URL_l127,	URL_l128,	URL_l129,	URL_l130,	URL_l131,	URL_l132,	URL_l133,	URL_l134,	URL_l135,	URL_l136,	URL_l137,	URL_l138,	URL_l139,	URL_l140,	URL_l141,	URL_l142,	URL_l143,	URL_l144,	URL_l145,	URL_l146,	URL_l147,	URL_l148,	URL_l149,	URL_l150,	URL_l151,	URL_l152,	URL_l153,	URL_l154,	URL_l155,	URL_l156,	URL_l157,	URL_l158,	URL_l159,	URL_l160,	URL_l161,	URL_l162,	URL_l163,	URL_l164,	URL_l165,	URL_l166,	URL_l167,	URL_l168,	URL_l169,	URL_l170,	URL_l171,	URL_l172,	URL_l173,	URL_l174,	URL_l175,	URL_l176,	URL_l177,	URL_l178,	URL_l179,	URL_l180,	URL_l181,	URL_l182,	URL_l183,	URL_l184,	URL_l185,	URL_l186,	URL_l187,	URL_l188,	URL_l189,	URL_l190,	URL_l191,	URL_l192,	URL_l193,	URL_l194,	URL_l195,	URL_l196,	URL_l197,	URL_l198,	URL_l199,	URL_l200,	URL_l201,	URL_l202,	URL_l203,	URL_l204,	URL_l205,	URL_l206,	URL_l207,	URL_l208,	URL_l209,	URL_l210,	URL_l211,	URL_l212,	URL_l213,	URL_l214,	URL_l215,	URL_l216,	URL_l217,	URL_l218,	URL_l219,	URL_l220,	URL_l221,	URL_l222,	URL_l223,	URL_l224,	URL_l225,	URL_l226,	URL_l227,	URL_l228,	URL_l229,	URL_l230,	URL_l231,	URL_l232,	URL_l233,	URL_l234,	URL_l235,	URL_l236,	URL_l237,	URL_l238,	URL_l239,	URL_l240,	URL_l241,	URL_l242,	URL_l243,	URL_l244,	URL_l245,	URL_l246,	URL_l247,	URL_l248,	URL_l249,	URL_l250,	URL_l251,	URL_l252,	URL_l253,	URL_l254,	URL_l255,	URL_l256,	URL_l257,	URL_l258,	URL_l259,	URL_l260]

# Fill in this dictionary with your personal details!
JOB_APP = {
    "first_name": "Anandha",
    "last_name": "Rajendran",
    "email": "ranandh87@gmail.com",
    "phone": "503-383-9048",
    "org": "eBay",
    "resume": "resume.pdf",
    "resume_textfile": "resume_short.txt",
    "linkedin": "https://www.linkedin.com/in/ranandha/",
    "website": "",
    "github": "",
    "twitter": "",
    "location": "Portland, Oregon, United States",
    "grad_month": '06',
    "grad_year": '2014',
    "university": "San Jose State University"  # if only o.O
}


# Greenhouse has a different application form structure than Lever, and thus must be parsed differently
def greenhouse(driver):
    # basic info
    driver.find_element_by_id('first_name').send_keys(JOB_APP['first_name'])
    driver.find_element_by_id('last_name').send_keys(JOB_APP['last_name'])
    driver.find_element_by_id('email').send_keys(JOB_APP['email'])
    driver.find_element_by_id('phone').send_keys(JOB_APP['phone'])

    # This doesn't exactly work, so a pause was added for the user to complete the action
    try:
        loc = driver.find_element_by_id('job_application_location')
        loc.send_keys(JOB_APP['location'])
        # loc.send_keys(Keys.DOWN)  # manipulate a dropdown menu
        # loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.RETURN)
        # time.sleep(2) # give user time to manually input if this fails

    except NoSuchElementException:
        pass

    # Upload Resume as a Text File
    driver.find_element_by_css_selector("[data-source='paste']").click()
    resume_zone = driver.find_element_by_id('resume_text')
    resume_zone.click()
    with open(JOB_APP['resume_textfile']) as f:
        lines = f.readlines()  # add each line of resume to the text area
        for line in lines:
            resume_zone.send_keys(line)
            time.sleep(2)

            # Upload coverletter as a Text File
        driver.find_element_by_xpath("//*[@id='main_fields']/div[9]/div/div[3]/a[3]").click()
        cover_letter_zone = driver.find_element_by_id('cover_letter_text')
        cover_letter_zone.click()
        with open(JOB_APP['resume_textfile']) as f:
            lines = f.readlines()  # add each line of resume to the text area
            for line in lines:
                cover_letter_zone.send_keys(line)
                time.sleep(2)

    # add linkedin
    try:
        driver.find_element_by_xpath("//label[contains(.,'LinkedIn')]").send_keys(JOB_APP['linkedin'])
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath("//label[contains(.,'Linkedin')]").send_keys(JOB_APP['linkedin'])
        except NoSuchElementException:
            pass

    # #school details
    # try:
    #   school = driver.find_element_by_xpath("//*[@id='s2id_education_school_name_0']/a/span[1]").send_keys(JOB_APP['university'])
    #   school.send_keys(Keys.DOWN)
    #   school.send_keys(Keys.RETURN)
    # except NoSuchElementException:
    #     pass

    # where do you live
    try:
        driver.find_element_by_css_selector("#job_application_answers_attributes_2_text_value").send_keys(
            "Portland,Oregon,USA")
    except NoSuchElementException:
        pass

    # legal
    try:
        driver.find_element_by_css_selector(
            "#s2id_job_application_answers_attributes_4_boolean_value > a > span.select2-chosen")
        driver.find_element_by_xpath(
            "//*[@id='s2id_job_application_answers_attributes_4_boolean_value']/a/span[2]/b").click()
        driver.find_element_by_xpath("//*[@id='select2List0']/li[2]/div").click()
    except NoSuchElementException:
        pass

    # Age 18
    try:
        DropDownSelection = driver.find_element_by_css_selector(
            "#s2id_job_application_answers_attributes_5_boolean_value > a")
        driver.find_element_by_xpath(
            "//*[@id='s2id_job_application_answers_attributes_5_boolean_value']/a/span[2]").click()
        DropDownSelection.send_keys(Keys.ARROW_DOWN)
        DropDownSelection.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    # Why are you interested in this position?
    driver.find_element_by_css_selector("#job_application_answers_attributes_7_text_value").send_keys(
        "Passionate to build product which would have a good impact to humanity using technology with professional and academic experience.")

    # can you relocate
    try:
        driver.find_element_by_xpath("//*[@id='job_application_answers_attributes_3_text_value']").send_keys("Yes")
    except NoSuchElementException:
        pass

    # accommodation

    try:
        driver.find_element_by_css_selector(
            "#s2id_job_application_answers_attributes_6_boolean_value > a > span.select2-chosen")
        driver.find_element_by_xpath("//*[@id='s2id_job_application_answers_attributes_6_boolean_value']/a").click()
        driver.find_element_by_xpath('//*[@id="select2List2"]/li[2]/div').click()
    except NoSuchElementException:
        pass

    # Have you ever been interviewed for a position
    try:
        interviewed = driver.find_element_by_css_selector(
            "#s2id_job_application_answers_attributes_8_boolean_value > a > span.select2-chosen")
        driver.find_element_by_css_selector(
            "#s2id_job_application_answers_attributes_8_boolean_value > a > span.select2-arrow > b").click()
        driver.find_element_by_xpath("//*[@id='select2List3']/li[2]/div").click()
    except NoSuchElementException:
        pass

    # add graduation year
    try:
        driver.find_element_by_xpath("//select/option[text()='2021']").click()
    except NoSuchElementException:
        pass

    # add university
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Harvard')]").click()
    except NoSuchElementException:
        pass

    # add degree
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Bachelor')]").click()
    except NoSuchElementException:
        pass

    # add major
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'Computer Science')]").click()
    except NoSuchElementException:
        pass

    # add website
    try:
        driver.find_element_by_xpath("//label[contains(.,'Website')]").send_keys(JOB_APP['website'])
    except NoSuchElementException:
        pass

    # add work authorization
    try:
        driver.find_element_by_xpath("//select/option[contains(.,'any employer')]").click()
    except NoSuchElementException:
        pass

    driver.find_element_by_id("submit_app").click()


# Handle a Lever form
def lever(driver):
    # navigate to the application page
    driver.find_element_by_class_name('template-btn-submit').click()

    # basic info
    first_name = JOB_APP['first_name']
    last_name = JOB_APP['last_name']
    full_name = first_name + ' ' + last_name  # f string didn't work here, but that's the ideal thing to do
    driver.find_element_by_name('name').send_keys(full_name)
    driver.find_element_by_name('email').send_keys(JOB_APP['email'])
    driver.find_element_by_name('phone').send_keys(JOB_APP['phone'])
    driver.find_element_by_name('org').send_keys(JOB_APP['org'])

    # socials
    driver.find_element_by_name('urls[LinkedIn]').send_keys(JOB_APP['linkedin'])
    driver.find_element_by_name('urls[Twitter]').send_keys(JOB_APP['twitter'])
    try:  # try both versions
        driver.find_element_by_name('urls[Github]').send_keys(JOB_APP['github'])
    except NoSuchElementException:
        try:
            driver.find_element_by_name('urls[GitHub]').send_keys(JOB_APP['github'])
        except NoSuchElementException:
            pass
    driver.find_element_by_name('urls[Portfolio]').send_keys(JOB_APP['website'])

    # add university
    try:
        driver.find_element_by_class_name('application-university').click()
        search = driver.find_element_by_xpath("//*[@type='search']")
        search.send_keys(JOB_APP['university'])  # find university in dropdown
        search.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    # Compensation

    try:
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[3]/ul/li[12]/label/div[2]/input").send_keys(
            "Negotiable")
        time.sleep(5)
    except NoSuchElementException:
        pass

    # add how you found out about the company
    try:
        driver.find_element_by_class_name('application-dropdown').click()
        search = driver.find_element_by_xpath("//select/option[text()='Glassdoor']").click()
    except NoSuchElementException:
        pass

    # submit resume last so i   t doesn't auto-fill the rest of the form
    # since Lever has a clickable file-upload, it's easier to pass it into the webpage
    driver.find_element_by_name('resume').send_keys(os.getcwd() + "/resume.pdf")
    driver.find_element_by_class_name('template-btn-submit').click()


def aggregrate_urls():
    print(f'Job Listings: {aggregatedURLs}')
    print('\n')
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    for url in aggregatedURLs:
        print('\n')

        if 'greenhouse' in url:
            driver.get(url)
            try:
                greenhouse(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                # print(f"FAILED FOR {url}")
                continue

        elif 'lever' in url:
            driver.get(url)
            try:
                lever(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                # print(f"FAILED FOR {url}")
                continue
        # i dont think this else is needed
        else:
            # print(f"NOT A VALID APP LINK FOR {url}")
            continue

        time.sleep(1)  # can lengthen this as necessary (for captcha, for example)
    driver.close()


def defined_urls():
    print(f'Job Listings: {URLS}')
    print('\n')
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    for url in URLS:
        print('\n')

        if 'greenhouse' in url:
            driver.get(url)
            try:
                greenhouse(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                print(f"FAILED FOR {url}")
                continue

        elif 'lever' in url:
            driver.get(url)
            try:
                lever(driver)
                print(f'SUCCESS FOR: {url}')
            except Exception:
                # print(f"FAILED FOR {url}")
                continue
        # i dont think this else is needed
        else:
            # print(f"NOT A VALID APP LINK FOR {url}")
            continue

        time.sleep(5)  # can lengthen this as necessary (for captcha, for example)
    driver.close()


if __name__ == '__main__':
    # call get_links to automatically scrape job listings from glassdoor
    # comment below two lines if you think need not collect one page links or 5 page links and apply for only defined Urls
    # aggregatedURLs = getlinks.collectURLs()
    # aggregrate_urls()
    # Testing purpose
    defined_urls()
