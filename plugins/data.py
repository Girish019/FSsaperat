
# A simple format under pic
FOMET = """
Ꮛᴘɪᴤοᴅє ŋο   ➺  <b>[{}] ,  {}</b>

▬▬▬▬▬ ✮✯☆★ ❂ ★☆✯✮ ▬▬▬▬▬
       
𝕯𝖆𝖙𝖊 ➻ <b>{}</b>

             𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐛𝐲  ➠  @Dot_serials_bot 

                       ⚜⚜⚜⍟⚜⚜⚜    
 
    YOUR EPISODE LINK 🔗 
<b>{}</b>
<b>{}</b>

        👀👩‍💻 𝐇𝐨𝐰 𝐭𝐨 𝐨𝐩𝐞𝐧 👩‍💻👀
https://t.me/+Sb5ro1gyhgY0NWM1
https://t.me/+Sb5ro1gyhgY0NWM1
  """
# A simple format return sent elements datails see (line 72, 39 in pluggins->channel post)
BOTEFITMSG = """
Post Sent Successfully ✅
Elements in <b>"{}{}"</b>

<b>TG Link : <a href="{}">Tlink</a></b> & <b>Short Link: <a href="{}">SLink</a></b>
<b>Vid Size : {}</b>   <b>Date : {}</b>
"""
#whole serials data return in dictionary
############{'serial name':["pic", "short link domin", "short link api", "To channel id"]}###############
#ex =>>>    '':['','','','']
DATAODD = {
        'Radhaku_Neevera_Praanam_':['https://graph.org/file/dc119c8d45919db61181c.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001942664190'],
#        'Gundamma_Katha_':['https://graph.org/file/baff21a920cc09f0ba89a.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001942664190'],
        'Rajeshwari_Vilas_Coffee_Club_':['https://graph.org/file/15328d049e6d89a06030a.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001942664190'],
        'Ammayi_Garu_':['https://graph.org/file/2afa02552352eb1ad1654.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001942664190'],
        'Oohalu_Gusagusalade_':['https://graph.org/file/66f92045eece717617ac1.jpg','links4money.com','ba4f1e7f7cfbea8b02c4c031be2270e354e95d47','-1001942664190'],
        'Maa_Varu_Mastaaru_':['https://graph.org/file/0c7b76e2ffba37dc80f24.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001942664190'],
        'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/2a210b8e8c9c008a21626.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001942664190'],
        'Seethe_Ramudi_Katnam_':['https://graph.org/file/40879ee73f036312ebb91.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1001942664190'],
        'Jagadhatri_':['https://graph.org/file/ea7b3f138cbb1cbf89328.jpg','linkshortify.com','9e82f5e0d917c633234194f39c2985752efd67e0','-1001942664190'],
 #       'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/979b1125f1b333d1b8b07.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001942664190'],
        'Trinayani_':['https://graph.org/file/db548886e1746a102b62a.jpg','links4money.com','ba4f1e7f7cfbea8b02c4c031be2270e354e95d47','-1001942664190'],
        'Radhamma_Kuthuru_':['https://graph.org/file/edffb4f77446259b8ca5e.jpg','tnshort.net','0045de7eda3a082a38f05bdd0d1c4de1262709fb','-1001942664190'],
        'Prema_Entha_Maduram_':['https://graph.org/file/875789bddf3b18111a8b1.jpg','linkshortify.com','8a9a3df5db074b2b1ad10efcd383e5243118447b','-1001942664190'],
        'Nindu_Noorella_Saavasam_':['https://graph.org/file/6bf07ca5c1fd598b73478.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001942664190'],
        'Subhasya_Seeghram_':['https://graph.org/file/9a8a693eca9c41a57bade.jpg','moneycase.link','f35b0c3ac535a200b3287c698b652e58b4689b6f','-1001942664190'],
        
  #      'Soubhagyavati_Bhava_':['https://graph.org/file/2d34fb7705e6ecb7c5937.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001942664190'],
  #      'Hitler_Kalyana_':['https://graph.org/file/4bccb3c8fd1fe4c5d92e7.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1001942664190'],
   #     'Sathya_':['https://graph.org/file/7f30ff54ecf9b380e4634.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1001942664190'],
    #    'Dance_Karnataka_Dance_Season_7_':['https://graph.org/file/2d724f7a19f736c405990.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001942664190'],
   #     'Bharjari_Bachelors_':['https://graph.org/file/1b28fb7863cc31f732ac4.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001942664190'],
    #    'Couples_Kitchen_':['https://graph.org/file/07d7a9c7707eac7367842.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001942664190'],
    #    'Chota_Champion_':['https://graph.org/file/0d77fc85da98174336f8b.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001942664190'],
    #    'Jodi_No_1_Season_2_':['https://graph.org/file/034b0251e3e3cbc172ddf.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001942664190'],

  
        'Pavada_Purasha_':['https://graph.org/file/f65651907ba441187f7b1.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001965277713'],
        'Olavina_Nildana_':['https://graph.org/file/441e02c5e145609e0eedd.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001965277713'],
        'Kendasampige_':['https://graph.org/file/62c90177d09f7cf416e6c.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001965277713'],
        'Bhagyalakshmi_':['https://graph.org/file/261d0c995b5e2a434093b.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1001965277713'],
        'Ramachari_':['https://graph.org/file/f590c3585b4c0068df630.jpg','tnshort.net','0045de7eda3a082a38f05bdd0d1c4de1262709fb','-1001965277713'],
        'Lakshmi_Baramma_':['https://graph.org/file/be3588e70978523792514.jpg','linkshortify.com','9e82f5e0d917c633234194f39c2985752efd67e0','-1001965277713'],
        'Geetha_':['https://graph.org/file/e95baeeafbf180bd184e1.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1001965277713'],
        'Lakshana_':['https://graph.org/file/995a7a33f5d543f4f4dbf.jpg','linkshortify.com','8a9a3df5db074b2b1ad10efcd383e5243118447b','-1001965277713'],
        'Punyavathi_':['https://graph.org/file/c15998a362846c9eb09f0.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001965277713'],
        'Tripura_Sundari_':['https://graph.org/file/4a59fd893093b82e9c234.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001965277713'],
        'Antarapata_':['https://graph.org/file/ea08c222d4848f1661e3c.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1001965277713'],
        'Gruhapravesha_':['https://graph.org/file/16220456e337fa35b18b7.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001965277713'],
        'Ganda_Hendthi_':['https://graph.org/file/e7437d0a9eac55fdb2623.jpg','moneycase.link','f35b0c3ac535a200b3287c698b652e58b4689b6f','-1001965277713'],
        'Shantham_Papam_':['https://graph.org/file/fa897d25d4d944e8487d5.jpg','links4money.com','ba4f1e7f7cfbea8b02c4c031be2270e354e95d47','-1001965277713'],
        'Muddu_Bangara_':['https://graph.org/file/49001901d7ccbf8698935.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001965277713'],
        'Gunasundari_':['https://graph.org/file/8d4b6b2e9703a7d97b546.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001965277713'],
        'Anu_':['https://graph.org/file/7a8f5ce25159932859193.jpg','onepagelink.in','5b9b84dfbc7b58a84ae25a75e2b5cf4fec69a4eb','-1001965277713'],
        'Family_Gangstars_':['https://graph.org/file/d08c55a1b259a3b5c95b7.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001965277713'],

        'Neenadhe_Naa_':['https://graph.org/file/fcbbf0a8c0413d4a59ad9.jpg','tnshort.net','0045de7eda3a082a38f05bdd0d1c4de1262709fb','-1001901182731'],
        'Namma_Lachi_':['https://graph.org/file/b315e59c10e04d1b2e595.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1001901182731'],
        'Nagapanchami_':['https://graph.org/file/dd2a58d339ca517010edc.jpg','linkshortify.com','8a9a3df5db074b2b1ad10efcd383e5243118447b','-1001901182731'],
        'Raani_':['https://graph.org/file/5a8aed0bcd6e14604b5d8.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1001901182731'],
        'Katheyondu_Shuruvagide_':['https://graph.org/file/e9b9f1a3dd7bc26772d5c.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001901182731'],
        'O_MuddhuManase_':['https://graph.org/file/cd2664a143bec7e2d5f14.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1001901182731'],
        'Jenugudu_':['https://graph.org/file/48a8df66387287f6e2440.jpg','linkshortify.com','9e82f5e0d917c633234194f39c2985752efd67e0','-1001901182731'],
        'Udho_Udho_Shri_Renuka_Yellamma_':['https://graph.org/file/f5749c1343173f855b0e7.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001901182731'],
        'Aragini_2_':['https://graph.org/file/6ddd25521aa2c813306aa.jpg','moneycase.link','f35b0c3ac535a200b3287c698b652e58b4689b6f','-1001901182731'],
        'Honganasu_':['https://graph.org/file/ca9bcfcfb5560459c3bcf.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001901182731'],
        'Anuraga_Aralitu_':['https://graph.org/file/0b15dd8c7f1d0118af62e.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001901182731'],
        'Anupama_Sarvagunaa_Sampanne_':['https://graph.org/file/0e86ebb3ab5cf24eac6c9.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001901182731'],
        'Yediyur_Shree_Siddhalingeshwara_':['https://graph.org/file/20ff06892579f4e3ac9ed.jpg','links4money.com','ba4f1e7f7cfbea8b02c4c031be2270e354e95d47','-1001901182731'],
        'Bombat_Bhojana_':['https://graph.org/file/d2871411e7358e4c76b52.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001901182731'],
        'Suvarna_Superstar_':['https://graph.org/file/09f90f559d100a415f393.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001901182731'],
        'Kaveri_Kannada_Medium_':['https://graph.org/file/b53472a77d733b99b2f05.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001901182731']
}
DATAEVEN = {
        'Radhaku_Neevera_Praanam_':['https://graph.org/file/dc119c8d45919db61181c.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001942664190'],
#        'Gundamma_Katha_':['https://graph.org/file/baff21a920cc09f0ba89a.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001942664190'],
        'Rajeshwari_Vilas_Coffee_Club_':['https://graph.org/file/15328d049e6d89a06030a.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001942664190'],
        'Ammayi_Garu_':['https://graph.org/file/2afa02552352eb1ad1654.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001942664190'],
        'Oohalu_Gusagusalade_':['https://graph.org/file/66f92045eece717617ac1.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001942664190'],
        'Maa_Varu_Mastaaru_':['https://graph.org/file/0c7b76e2ffba37dc80f24.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001942664190'],
        'Chiranjeevi_Lakshmi_Sowbhagyavati_':['https://graph.org/file/2a210b8e8c9c008a21626.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001942664190'],
        'Jagadhatri_':['https://graph.org/file/ea7b3f138cbb1cbf89328.jpg','linkshortify.com','9e82f5e0d917c633234194f39c2985752efd67e0','-1001942664190'],
        'Trinayani_':['https://graph.org/file/db548886e1746a102b62a.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1001942664190'],
        'Radhamma_Kuthuru_':['https://graph.org/file/edffb4f77446259b8ca5e.jpg','links4money.com','ba4f1e7f7cfbea8b02c4c031be2270e354e95d47','-1001942664190'],
        'Prema_Entha_Maduram_':['https://graph.org/file/875789bddf3b18111a8b1.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001942664190'],
        'Nindu_Noorella_Saavasam_':['https://graph.org/file/6bf07ca5c1fd598b73478.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1001942664190'],
        'Subhasya_Seeghram_':['https://graph.org/file/9a8a693eca9c41a57bade.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1001942664190'],
        'Seethe_Ramudi_Katnam_':['https://graph.org/file/40879ee73f036312ebb91.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001942664190'],
    
#        'Shrirasthu_Shubhamasthu_':['https://graph.org/file/b6d93c7cc15166fbf7e35.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001942664190'],
 #       'Soubhagyavati_Bhava_':['https://graph.org/file/2d34fb7705e6ecb7c5937.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001942664190'],
 #       'Hitler_Kalyana_':['https://graph.org/file/4bccb3c8fd1fe4c5d92e7.jpg','tnshort.net','0045de7eda3a082a38f05bdd0d1c4de1262709fb','-1001942664190'],
 #       'Sathya_':['https://graph.org/file/7f30ff54ecf9b380e4634.jpg','linkshortify.com','8a9a3df5db074b2b1ad10efcd383e5243118447b','-1001942664190'],
 #       'Dance_Karnataka_Dance_Season_7_':['https://graph.org/file/2d724f7a19f736c405990.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001942664190'],
 #       'Bharjari_Bachelors_':['https://graph.org/file/1b28fb7863cc31f732ac4.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001942664190'],
 #       'Couples_Kitchen_':['https://graph.org/file/07d7a9c7707eac7367842.jpg','moneycase.link','f35b0c3ac535a200b3287c698b652e58b4689b6f','-1001942664190'],
 #       'Chota_Champion_':['https://graph.org/file/0d77fc85da98174336f8b.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001942664190'],
 #       'Jodi_No_1_Season_2_':['https://graph.org/file/034b0251e3e3cbc172ddf.jpg','moneycase.link','f35b0c3ac535a200b3287c698b652e58b4689b6f','-1001942664190'],
  
        'Pavada_Purasha_':['https://graph.org/file/f65651907ba441187f7b1.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001965277713'],
        'Olavina_Nildana_':['https://graph.org/file/441e02c5e145609e0eedd.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001965277713'],
        'Kendasampige_':['https://graph.org/file/62c90177d09f7cf416e6c.jpg','links4money.com','ba4f1e7f7cfbea8b02c4c031be2270e354e95d47','-1001965277713'],
        'Bhagyalakshmi_':['https://graph.org/file/261d0c995b5e2a434093b.jpg','tnshort.net','0045de7eda3a082a38f05bdd0d1c4de1262709fb','-1001965277713'],
        'Ramachari_':['https://graph.org/file/f590c3585b4c0068df630.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1001965277713'],
        'Lakshmi_Baramma_':['https://graph.org/file/be3588e70978523792514.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1001965277713'],
        'Geetha_':['https://graph.org/file/e95baeeafbf180bd184e1.jpg','linkshortify.com','9e82f5e0d917c633234194f39c2985752efd67e0','-1001965277713'],
        'Lakshana_':['https://graph.org/file/995a7a33f5d543f4f4dbf.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1001965277713'],
        'Punyavathi_':['https://graph.org/file/c15998a362846c9eb09f0.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001965277713'],
        'Tripura_Sundari_':['https://graph.org/file/4a59fd893093b82e9c234.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001965277713'],
        'Antarapata_':['https://graph.org/file/ea08c222d4848f1661e3c.jpg','linkshortify.com','8a9a3df5db074b2b1ad10efcd383e5243118447b','-1001965277713'],
        'Gruhapravesha_':['https://graph.org/file/16220456e337fa35b18b7.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001965277713'],
        'Ganda_Hendthi_':['https://graph.org/file/e7437d0a9eac55fdb2623.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001965277713'],
        'Shantham_Papam_':['https://graph.org/file/fa897d25d4d944e8487d5.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001965277713'],
        'Muddu_Bangara_':['https://graph.org/file/49001901d7ccbf8698935.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001965277713'],
        'Gunasundari_':['https://graph.org/file/8d4b6b2e9703a7d97b546.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001965277713'],
        'Anu_':['https://graph.org/file/7a8f5ce25159932859193.jpg','links4money.com','2853363dbc172344dd8b979c9ff097d2a0ff4714','-1001965277713'],
        'Family_Gangstars_':['https://graph.org/file/d08c55a1b259a3b5c95b7.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001965277713'],

        'Neenadhe_Naa_':['https://graph.org/file/fcbbf0a8c0413d4a59ad9.jpg','linkshortify.com','4bc6f1e34d0409e5b8bd2197d42462bb1ec6048a','-1001901182731'],
        'Namma_Lachi_':['https://graph.org/file/b315e59c10e04d1b2e595.jpg','tnshort.net','0045de7eda3a082a38f05bdd0d1c4de1262709fb','-1001901182731'],
        'Nagapanchami_':['https://graph.org/file/dd2a58d339ca517010edc.jpg','tnshort.net','1183b34c88b1fd4e898d7d9dc7b6fc6a2bea9dd9','-1001901182731'],
        'Raani_':['https://graph.org/file/5a8aed0bcd6e14604b5d8.jpg','linkshortify.com','9e82f5e0d917c633234194f39c2985752efd67e0','-1001901182731'],
        'Katheyondu_Shuruvagide_':['https://graph.org/file/e9b9f1a3dd7bc26772d5c.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001901182731'],
        'O_MuddhuManase_':['https://graph.org/file/cd2664a143bec7e2d5f14.jpg','linkshortify.com','8a9a3df5db074b2b1ad10efcd383e5243118447b','-1001901182731'],
        'Jenugudu_':['https://graph.org/file/48a8df66387287f6e2440.jpg','tnshort.net','cfafc72b0df2558f0f5ad4e1c906ce9f783281e3','-1001901182731'],
        'Udho_Udho_Shri_Renuka_Yellamma_':['https://graph.org/file/f5749c1343173f855b0e7.jpg','links4money.com','f2c99e727ba0a517e53f77a31b4f79d8acfc318c','-1001901182731'],
        'Aragini_2_':['https://graph.org/file/6ddd25521aa2c813306aa.jpg','tnvalue.in','e496ab76b42f51628da20bb69577397533008f3c','-1001901182731'],
        'Honganasu_':['https://graph.org/file/ca9bcfcfb5560459c3bcf.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001901182731'],
        'Anuraga_Aralitu_':['https://graph.org/file/0b15dd8c7f1d0118af62e.jpg','moneycase.link','0c2406a0cf1b54db75fcba4cbb8e389bdc675eee','-1001901182731'],
        'Anupama_Sarvagunaa_Sampanne_':['https://graph.org/file/0e86ebb3ab5cf24eac6c9.jpg','tnvalue.in','8fc4e5a5a7f1d571adfc7c02537d7c1e73da1a15','-1001901182731'],
        'Yediyur_Shree_Siddhalingeshwara_':['https://graph.org/file/20ff06892579f4e3ac9ed.jpg','links4money.com','668f8a8d31c4d5e55da03d0d21ae740f3caf5d14','-1001901182731'],
        'Bombat_Bhojana_':['https://graph.org/file/d2871411e7358e4c76b52.jpg','links4money.com','ba4f1e7f7cfbea8b02c4c031be2270e354e95d47','-1001901182731'],
        'Suvarna_Superstar_':['https://graph.org/file/09f90f559d100a415f393.jpg','tnvalue.in','ff426552eda72230153ea3450a0bce0557183ccb','-1001901182731'],
        'Kaveri_Kannada_Medium_':['https://graph.org/file/b53472a77d733b99b2f05.jpg','moneycase.link','bdc62bf7dd54515abf15371b58feb6a1ff2b434a','-1001901182731']
}
