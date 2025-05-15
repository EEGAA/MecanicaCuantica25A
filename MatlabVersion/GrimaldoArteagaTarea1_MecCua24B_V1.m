% Mecánica Cuántica II 24B 09/Nov/24 - TAREA 1 -
close all; clear; clc;
%% 
% ____Legendre____
theta = -pi: 0.01: pi;
%plm
 p11 = sin(theta);
 p10 = cos(theta);

 p22 = 3 .* sin(theta) .^2;
 p21 = 3 .* sin(theta) .* cos(theta);
 p20 = 1/2 .* (3 .* cos(theta) .^2 - 1);

 p33 = 15 .* sin(theta) .* (1 - cos(theta) .^2);
 p32 = 15 .* sin(theta) .^2 .* cos(theta);
 p31 = 3/2 .* sin(theta) .* (5 .*  cos(theta) .^2 - 1);
 p30 = 1/2 .* (5 .* cos(theta) .^3 - 3 .* cos(theta));

%%
% ____Rodríguez____
RGZ = cell(1,10);
syms x;
n = 1;
N = 10;
for i = n: N+1
    l = i - 1;
    Plx = 1/(2^l * factorial(l)) * diff(((x^2 - 1)^l), x, l);

    X = (-1: 0.001: 1);
    PlxG{i} = subs(Plx, x, X);
end
%Todas las ecuaciones anteriores fueron tomadas de la diapositiva
%%Parte del código correspondiente a la graficación
figure; 
subplot(331); polarplot(theta, p11); title('P_1^1')
subplot(332); polarplot(theta, p10); title('P_1^0')
subplot(333); polarplot(theta, p22); title('P_2^2')
subplot(334); polarplot(theta, p21); title('P_2^1')
subplot(335); polarplot(theta, p20); title('P_2_0')
subplot(336); polarplot(theta, p33); title('P_3^3')
subplot(337); polarplot(theta, p32); title('P_3^2')
subplot(338); polarplot(theta, p31); title('P_3^1')
subplot(339); polarplot(theta, p30); title('P_3^0')
figure;
subplot(331); polarplot(theta, p11); title('P_1^1')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];
subplot(332); polarplot(theta, p10); title('P_1^0')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];
subplot(333); polarplot(theta, p22); title('P_2^2')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];
subplot(334); polarplot(theta, p21); title('P_2^1')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];
subplot(335); polarplot(theta, p20); title('P_2^0')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];
subplot(336); polarplot(theta, p33); title('P_3^3')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];
subplot(337); polarplot(theta, p32); title('P_3^2')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];
subplot(338); polarplot(theta, p31); title('P_3^1')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];
subplot(339); polarplot(theta, p30); title('P_3^0')
ax = gca; ax.ThetaTickLabel = []; ax.RTickLabel = [];

figure;
for i = n: N+1
    hold on
    plot(X, double(PlxG{i}));
end

figure;
subplot(211); title('primeros 5 valores de "l"')
for i = n: N/2
    hold on
    plot(X, double(PlxG{i}));
end
subplot(212); title('Valores de "l" del 5 al 10')
for i = N/2: N
    hold on
    plot(X, double(PlxG{i}));
end
