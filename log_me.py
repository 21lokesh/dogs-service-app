navigation_helper = """ 
ScreenManager:
    FirstScreen:
    SecondScreen:
    ThirdScreen:
    FourthScreen:
    FifthScreen:
    SixthScreen:
    SeventhScreen:
    EighthScreen:
    NinthScreen:
    TenthScreen:
    
    
<FirstScreen>:           
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'eye-off'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
        password:True
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        #on_press:root.manager.current='google'
        on_release:app.signup()
         
<SecondScreen>:      
    md_bg_color:[0,0,0.5,1]
    name:'google'
    id:'google' 
    MDCard:
        size_hint:None,None
        size:320,500
        pos_hint:{"center_x":0.5,"center_y":0.5}
        elevation:8
        md_bg_color:[0,0,2,1]
        padding:20
        spacing:30
        orientation:'vertical'

        MDLabel:
            text:'Phone Number'
            font_style:'Button'
            font_size:45
            halign:'center'
            size_hint_y:None
            height:self.texture_size[1]
            padding_y:15
            
        MDTextField:
            id:name
            hint_text:"Name"
            mode:"fill"
            icon_right:"account"    
            size_hint_x:None
            helper_text:'Required'
            helper_text_mode:'on_error'
            width:220
            font_size:20
            pos_hint:{'center_x':0.5}
            color_active:[1,1,1,1]
            required:False
 

        MDTextField:
            id:phone
            hint_text:"phone Number"
            mode:"fill"
            icon_right:"phone"    
            size_hint_x:None
            helper_text:'Required'
            helper_text_mode:'on_error'
            width:220
            font_size:20
            pos_hint:{'center_x':0.5}
            color_active:[1,1,1,1]
            required:False

        MDFillRoundFlatIconButton:
            text:"Next"
            icon:'arrow-right'
            pos_hint:{"center_x":0.5,"center_y":0.4}
            #on_press:app.phone_number()
            on_press:root.manager.current='screen_app'

        MDFillRoundFlatIconButton:
            text:'Login With Google'
            icon:'google'
            pos_hint:{'center_x':0.5,'center_y':0.5}
            font_size:15
            on_release:app.login()
        #MDProgressBar:
        #    value:60
         #   pos_hint:{'center_y':0.02}
        
<ThirdScreen>:  
    name:'dob'
    MDLabel:
        text:'Dogs'
        halign:'center'
        pos_hint:{'center_y':0.8}
        font_style:'H3'
        
    MDRaisedButton:
        pos_hint:{'center_x':0.5,'center_y':0.1}
        text:'Load'
        on_press:app.load_img()
    MDGridLayout:
        cols:1
        adaptive_height:True
        padding:dp(20),dp(120)
        spacing:dp(20)
        MyTile:
            id:imgg
            source:""  
    MDFloatingActionButton:
        text:'Back'
        icon:'arrow-left'
        md_bg_color:0,1,0,1
        pos_hint:{'center_x':0.1,'center_y':0.9}
        on_press:root.manager.current='main'
        
    MDFillRoundFlatIconButton:
        text:"home"
        icon:'arrow-right'
        pos_hint:{'center_x':0.9,'center_y':0.2}
        on_press:root.manager.current='screen_app'
        

       
        
<FourthScreen>:           
    name:"main"
    Image:
        id:bck
        source:''
        size:root.size
    
        
    MDFillRoundFlatIconButton:
        text:"next"
        icon:'arrow-right'
        pos_hint:{"center_x":0.5,"center_y":0.2}
        on_press:root.manager.current='dob'
        
        
#different screens can add from here



<FifthScreen>:
    name:"screen_login"
    id: screen_login

    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text:"Congratulations Your Member of Our"
            halign:'center'
            pos_hint:{'center_x':0.5,'center_y':0.5}
            md_bg_color:0.5,0,0.6,1
            font_style:'H4'
            

        MDFillRoundFlatIconButton:
            text:"next"
            icon:"arrow-right-bold-circle"

            pos_hint:{'center_x':0.9,'center_y':0.2}
            on_press:root.manager.current='main'

            #new screen

<SixthScreen>:      
    name:"page3"
    id: page3
    ScrollView:
        size:self.size
        #do_scroll_y:True
        #do_scroll_x:False
        GridLayout:
            size_hint_y:None
            height:self.minimum_height
            width:self.minimum_width
            cols:1
            spacing:"20dp"
            padding:"20dp"
    
            MDList:
                id:task_item
            MDFillRoundFlatIconButton:
                text:"Done"
                icon:"check"
    
                pos_hint:{'center_x':0.9,'center_y':0.1}
                on_press:root.manager.current='screen_login'
            
        
    MDFloatingActionButton:
        text:'Back'
        icon:'arrow-left'
        md_bg_color:0,1,0,1
        pos_hint:{'center_x':0.1,'center_y':0.9}
        on_press:root.manager.current='screen_app'


            
<SeventhScreen>:
    name:"booking"
    id: booking
    ScrollView:
        size:self.size
        #do_scroll_y:True
        #do_scroll_x:False
        GridLayout:
            size_hint_y:None
            height:self.minimum_height
            width:self.minimum_width
            cols:1
            spacing:"20dp"
            padding:"20dp"
            MDCard:
                size_hint:None,None
                size:390,390
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:2
                #md_bg_color:[0,0,2,1]
                padding:20
                spacing:30
                orientation:'vertical'
                   
                MDLabel:
                    text: "......Book your doorstep service.......\\nContact Details:\\nPhone Number:9902113575\\nGmail:lokeshchinna2381@gmail.com\\nWhatsapp Number:9902113575"              
                    halign:'center'
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    md_bg_color:0.5,0.7,0,1
            MDCard:
                size_hint:None,None
                size:390,390
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:2
                #md_bg_color:[0,0,2,1]
                padding:20
                spacing:30
                orientation:'vertical'
                MDLabel:
                    text:"Bath"
                    font_style:"H3"
                    hailgn:'center'
                    
                MDLabel:
                    text:"Conditioning\\nDry\\nNail Clipping\\nEar Cleaning\\nPaw Massage\\nCombing"
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    font_style:'H6'
                    
            
                MDFillRoundFlatIconButton:
                    text:'Book'
                    icon:'dog'
                    pos_hint:{'center_x':0.5,'center_y':0.2}
                    on_press:root.manager.current='scroll'
            MDCard:
                size_hint:None,None
                size:390,390
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:2
                #md_bg_color:[0,0,2,1]
                padding:20
                spacing:30
                orientation:'vertical'
                MDLabel:
                    text:"Body Haircut"
                    font_style:"H3"
                    hailgn:'center'
               
                MDLabel:
                    text:"Full Body Haircut\\nEar Cleaning\\nBody Wash\\nNail Cutting"
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    font_style:'H6'
                    
            
                MDFillRoundFlatIconButton:
                    text:'Book'
                    icon:'dog'
                    pos_hint:{'center_x':0.5,'center_y':0.2}
                    on_press:root.manager.current='scroll'
                          
            MDCard:
                size_hint:None,None
                size:390,390
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:2
                #md_bg_color:[0,0,2,1]
                padding:20
                spacing:30
                orientation:'vertical'
                MDLabel:
                    text:"Full Service"
                    font_style:"H3"
                    hailgn:'center'
               
                MDLabel:
                    text:"*Full body Haircut\\nBathing\\nEye Cleaning\\nNail Cutting\\nEar Cleaning\\nBody Dry\\nBody Massage\\nTeeth Cleaning\\npaw Massage\\nCombing"
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    font_style:'H6'
                    
            
                MDFillRoundFlatIconButton:
                    text:'Book'
                    icon:'dog'
                    pos_hint:{'center_x':0.5,'center_y':0.2}
                    on_press:root.manager.current='scroll'
                    
    MDFloatingActionButton:
        text:'Back'
        icon:'arrow-left'
        md_bg_color:0,1,0,1
        pos_hint:{'center_x':0.1,'center_y':0.9}
        on_press:root.manager.current='screen_app'

       
<NinthScreen>:
    name:'scroll'
    ScrollView:
        size:self.size
        #do_scroll_y:True
        #do_scroll_x:False
        GridLayout:
            size_hint_y:None
            height:self.minimum_height
            width:self.minimum_width
            cols:1
            spacing:"20dp"
            padding:"20dp"
            MDCard:
                size_hint:None,None
                size:398,420
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:1
                #md_bg_color:[0,0,2,1]
                padding:20
                spacing:30
                orientation:'vertical'
                MDLabel:
                    text:"Book Your Slot"
                    halign:'center'
                    font_style:"H3"
                    
                Image:
                    id: avatar
                    size_hint: None, None
                    #size: "56dp", "56dp"
                    source: "dog.png"
                    
                MDTextField:
                    id:task_text
                    hint_text:"add task"
                    pos_hint:{"center_y":0.4}
                    max_text_length:50
                    #on_text_validate:(app.add_task(task_text,date_text.text),app.
                    #close_dialog())

                MDRaisedButton:
                    id:date_picker
                    text:"Date Picker"
                    icon:'calendar'
                    user_font_size:'70sp'
                    pos_hint:{"center_x":0.2,"center_y":0.7}
                    on_release:app.show_date_picker()
            MDLabel:
                spacing:"10dp"
                id:date_text
            BoxLayout:
                orientation:"horizontal"
                
                
                MDIconButton:
                    icon:'check'
                    pos_hint:{"center_x":0.2,"center_y":0.7}
                    #md_bg_color:0,0,0,1
                    on_release:app.time_picker()
                    
                MDLabel:
                    id:my_time
                    text:"time please"
                    pos_hint:{"center_x":0.2,"center_y":0.7}
                    bold:True
                                    
                
            MDCard:
                size_hint:None,None
                size:390,600
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:1
                #md_bg_color:[0,0,2,1]
                padding:20
                spacing:30
                orientation:'vertical'
                MDLabel:
                    text:"task"
                    halign:'center'
                    font_style:"H3"
                    pos_hint:{"center_x":0.5,"center_y":0.5}
                    
                MDTextField:
                    id:task_date
                    hint_text:"Enter Date for Service"
                    #mode:"fill"   
                    size_hint_x:None
                    width:220
                    font_size:20
                    pos_hint:{'center_x':0.5}
               
                MDTextField:
                    id:time
                    hint_text:"Enter Time in between 7am to 7pm"
                    #mode:"fill"   
                    size_hint_x:None
                    width:220
                    font_size:20
                    pos_hint:{'center_x':0.5}
                   
                
                MDTextField:
                    id:task
                    hint_text:"Enter your Address"
                    #mode:"fill"   
                    size_hint_x:None
                    width:220
                    font_size:20
                    pos_hint:{'center_x':0.5}
                    
                MDFillRoundFlatIconButton:
                    text:"Next"
                    icon:'arrow-right'
                    pos_hint:{"center_x":0.5,"center_y":0.4}
                    on_press:app.address()

                  
                
    MDFloatingActionButton:
        text:'Back'
        icon:'arrow-left'
        md_bg_color:0,1,0,1
        pos_hint:{'center_x':0.1,'center_y':0.9}
        on_press:root.manager.current='screen_app'
           
<TenthScreen>:  
    name:"ten"
    ScrollView:
        size:self.size
        #do_scroll_y:True
        #do_scroll_x:False
        GridLayout:
            size_hint_y:None
            height:self.minimum_height
            width:self.minimum_width
            cols:1
            spacing:"20dp"
            padding:"20dp"
            MDCard:
                size_hint:None,None
                size:390,420
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:1
                #md_bg_color:[0,0,2,1]
                padding:20
                spacing:30
                orientation:'vertical'
                MDLabel:
                    text:"Fill Details"
                    halign:'center'
                    font_style:"H3"
                MDTextField:
                    id:pho
                    hint_text:"Enter Phone number to confirm service"
                    #mode:"fill"   
                    size_hint_x:None
                    width:220
                    font_size:20
                    pos_hint:{'center_x':0.5}
               
                MDTextField:
                    id:breed
                    hint_text:"Enter Dog Breed"
                    #mode:"fill"   
                    size_hint_x:None
                    width:220
                    font_size:20
                    pos_hint:{'center_x':0.5}
                MDRaisedButton:
                    text:'Done'
                    pos_hint:{'center_x':0.5,'center_y':0.2}
                    on_press:app.add_task()
                
    MDFloatingActionButton:
        text:'Back'
        icon:'arrow-left'
        md_bg_color:0,1,0,1
        pos_hint:{'center_x':0.1,'center_y':0.9}
        on_press:root.manager.current='screen_app'
         
<MyTile@MDSmartTile>
    size_hint_y:None
    height:"240dp"
    

                                                            
<EighthScreen>:   
    name:"screen_app"
    id: app_screens    
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: title_bar
            title: 'Protect Dogs'
            left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]
            right_action_items:[['weather-sunny',lambda x:app.blackwhite()]]
            md_bg_color:17,0.8,0.5,1
            elevation: 5
            height:'20dp'
        Widget:
        

    MDNavigationLayout:

        ScreenManager:
            id: scr

            MDScreen:

                name: 'home'
                id:'home'
                BoxLayout:
                    orientation: 'vertical'

                    MDLabel:
                        text: ''
                        halign:'center'
                        pos_hint:{'center_x':0.5,'center_y':2}

                    #problem here
                MDScreen:
                    
                    MDBottomNavigation:
                        panel_color:17,0.8,0.5,1
                        #bottom navigation screens 
                        MDBottomNavigationItem:
                            
                            name:'dog'
                            text:'Dog'
                            icon:'dog'
                            MDScreen:
                                ScrollView:
                                    do_scroll_y:True
                                    do_scroll_x:False
                                    BoxLayout:
                                        id:box1
                                        orientation:'vertical'
                                        size_hint_y:None
                                        height:1000
                                        
                                        MDCard:
                                            size_hint:None,None
                                            size:350,550
                                            pos_hint:{"center_x":0.5,"center_y":0.5}
                                            elevation:4
                                            #md_bg_color:[0,0,2,1]
                                            padding:20
                                            spacing:30
                                            orientation:'vertical'
                                   
            
                                            MDLabel:
                                                text:'Hey I am Hussky'
                                                halign:'center'
                                            Image:
                                                id: avatar
                                                size_hint: None, None
                                                #size: "56dp", "56dp"
                                                source: "dog.png"
            
            
                        MDBottomNavigationItem:
                            name:'cat'
                            text:'Cat'
                            icon:'cat'
                            MDScreen:
                                BoxLayout:
                                    orientation: 'vertical'

                                    FloatLayout:   
                                        Image:
                                            id: image
                                            source: ''
                        
                                        MDRoundFlatButton:
                                            text: "Upload Image"
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                                            on_press: app.file_manager_open()
                                        
                                                                                                                                                            
                                                               
                        MDBottomNavigationItem:
                            name:'Trending'
                            text:'Trending'
                            icon:'star'
                            MDScreen:
            
                                MDLabel:
                                    text:'Thanks!!'
                                    halign:'center'  
                                    type:'bottom'
                                    icon:'dog'
                                Image:
                                    id: avatar
                                    size_hint: None, None
                                    #size: "56dp", "56dp"
                                    source: "R.png"    
                        MDBottomNavigationItem:
                            name:'Shop'
                            text:'Shop'
                            icon:'store'
                            MDScreen:
            
                                MDLabel:
                                    text:'Buy something'
                                    halign:'center'  
                                    #type:'bottom'
                                    icon:'store'
                                Image:
                                    id: avatar
                                    size_hint: None, None
                                    #size: "56dp", "56dp"
                                    source: "subjects.png"    
                        MDBottomNavigationItem:
                            name:'Videos'
                            text:'Videos'
                            icon:'video-box'
                            MDScreen:
                            
            
                                MDLabel:
                                    text:'Traning Videos'
                                    halign:'center'  
                                    #type:'bottom'
                                    icon:'video'
                                Image:
                                    id: avatar
                                    size_hint: None, None
                                    #size: "56dp", "56dp"
                                    source: "subjects.png"              
                                                                       
            MDScreen:
                name: 'profile'
                BoxLayout:
                    orientation: 'vertical'

                    
                FloatLayout:   
                    Image:
                        id: image
                        source: ''
    
                    MDRoundFlatButton:
                        text: "Upload Image"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                        on_press: app.file_manager_open()
                        
                    
            MDScreen:
                name: 'contact'
                MDLabel:
                    text:'Sending successful message'
                    halign:'center'
                    pos_hint:{'center_y':0.8}
                    font_style:'H3'
                    
                MDFillRoundFlatIconButton:
                    text:"send message on whatsapp"
                    icon:'arrow-right'
                    pos_hint:{"center_x":0.5,"center_y":0.4}
                    on_release:app.whatsupmsg()
                                
                    
                    
                

            MDScreen:
                name: 'history'
                BoxLayout:
                    orientation: 'vertical'

                    MDLabel:
                        text: 'Some history text'
                        halign:'center'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        #md_bg_color:4,7,2,1
            MDScreen:
                name: 'upload'
                BoxLayout:
                    orientation: 'vertical'

                    MDLabel:
                        text: 'Upload your picture'
                        halign:'center'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        #md_bg_color:4,7,2,1

            MDScreen:
                name: 'service'
                BoxLayout:
                    orientation: 'vertical'

                    MDLabel:
                        text: 'All types of services'
                        halign:'center'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        #md_bg_color:4,7,2,1
    MDFloatingActionButton:
        text:'menu'
        icon:'menu'
        icon_color:0,0,0,1
        md_bg_color:17,0.8,0.5,1
        pos_hint:{'center_x':0.1,'center_y':0.95}
        on_press:nav_drawer.set_state('toggle')
                    
                            
    MDFloatingActionButton:
        text:'Book'
        icon:'plus'
        md_bg_color:0,0,80,1
        pos_hint:{'center_x':0.9,'center_y':0.2}
        on_press:root.manager.current='booking'


    MDNavigationLayout:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'         
            
                Image:
                    source: 'dog.png'
                    size_hint: .5, .3
                    pos_hint: {"center_x": 0.5}
            
                MDLabel:
                    text: 'Dogs'
                    font_style: 'H3'
                    size_hint_y: None
                    height: self.texture_size[1]
            
                MDLabel:
                    text: 'Husky'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]
            
            
                ScrollView:
                    MDList:
            
                        OneLineIconListItem:
                            text: 'Home'
                            on_press: scr.current= 'home'
            
                            IconLeftWidget:
                                icon: 'home'
                                on_press: scr.current= 'home'
                        OneLineIconListItem:
                            text: 'Profile'
                            on_press: scr.current= 'profile'
            
                            IconLeftWidget:
                                icon: 'account'
                                on_press: scr.current= 'profile'
            
                        OneLineIconListItem:
                            text: 'Contact'
                            on_press: scr.current= 'contact'
            
                            IconLeftWidget:
                                icon: 'phone'
                                on_press: scr.current= 'contact'
            
                        OneLineIconListItem:
                            text: 'Recent'
                            on_press: scr.current= 'history'
            
                            IconLeftWidget:
                                icon: 'history'
                                on_press: scr.current= 'history'
            
                        OneLineIconListItem:
                            text: 'Upload'
                            on_press: scr.current= 'upload'
            
                            IconLeftWidget:
                                icon: 'upload'
                                on_press: scr.current= 'upload'
            
                        OneLineIconListItem:
                            text: ' Service'
                            on_press: scr.current= 'service'
            
                            IconLeftWidget:
                                icon: 'briefcase'
                                on_press: scr.current= 'service'
            
            
            MDFloatingActionButton:
                icon:"human"
                pos_hint:{'center_x':0.9,'center_y':0.2}
                user_font_size:'100sp'       
                on_press:app.bottom_layer()  
    

"""