clc, clear all, close all
x=videoinput('winvideo',1);
while(1)
    dato=importdata('say.txt'); 
    if (dato(1,1)==1)
        for i=1:1
            img=getsnapshot(x);
            fname=['Imagen',num2str(i)];
            imwrite(img,fname,'.jpg')
            pause(2);
        end
        break;
    end
end
disp('Foto capturada')