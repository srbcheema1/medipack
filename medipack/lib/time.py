class Time:
    def get_time(st):
        st = st.split(':')
        if(len(st) == 1):
            return None
        if(len(st) == 2):
            h='00'
            m,s = st
        if(len(st)==3):
            h,m,s = st
        if(len(st)>3):
            return None

        if(not Time._is_int(h) or not Time._is_int(m)):
            return None
        h = int(h)
        m = int(m)
        s = int(s)
        if(m>59 or s>59):
            return None
        return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)

    def get_relative_time(st,et):
        # just for safety
        st = Time.get_time(st)
        et = Time.get_time(et)

        st = st.split(':')
        sh,sm,ss = st

        et = et.split(':')
        eh,em,es = et

        sh = int(sh)
        sm = int(sm)
        ss = int(ss)

        eh = int(eh)
        em = int(em)
        es = int(es)

        if(es < ss):
            if(em == 0):
                if(eh == 0): return None
                eh -= 1
                em += 60
            em -= 1
            es +=60
        s = es - ss

        if(em < sm):
            if(eh == 0):return None
            eh -= 1
            em += 60
        m = em - sm

        if(eh < sh): return None
        h = eh - sh

        if(h == 0 and m == 0 and s == 0): return None
        return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)


    def _is_int(x):
        try:
            x = int(x)
        except:
            return False
        return True
