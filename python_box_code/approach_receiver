class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)


    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        import almath
        session = self.session()
        motion_service = session.service("ALMotion")

        # 3.Approach Receiver
        #time.sleep(2.0)
        self.logger.info("3.approach receiver")
        motion_service.setStiffnesses("Head", 1.0)
        motion_service.setStiffnesses("RArm", 1.0)
        names            = ["HeadYaw","HeadPitch","RElbowRoll","RShoulderPitch","RElbowYaw","RShoulderRoll"]
        angles           = [0.0*almath.TO_RAD,0.0*almath.TO_RAD,50.0*almath.TO_RAD,40.0*almath.TO_RAD,100.0*almath.TO_RAD,-5.0*almath.TO_RAD]
        fractionMaxSpeed = [0.1]*6
        motion_service.setAngles(names,angles,fractionMaxSpeed)
        time.sleep(3.0)

        #motion_service.setStiffnesses("Head", 0.0)
        #motion_service.setStiffnesses("RArm", 0.0)
        self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
